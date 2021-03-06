import sys
import pygame
from Modules import bullet
from Modules import Alien
from time import sleep
import threading
from playsound import playsound


class mythread(threading.Thread):
    def __init__(self,playsound):
        threading.Thread.__init__(self)
        self.playsound = playsound
        #self.collision = collision

    def run(self):
        
         
         playsound(self.playsound)
         #playsound(self.collision)

    
def play_collision():
    thread1 = mythread('Sound/explosion.mp3')
    thread1.start()

def play_fire():
    thread1 = mythread('Sound/Gun+Silencer.mp3')
    thread1.start()


def check_keydown_events(event,ai_settings,screen,ship,bullets):

            if event.key == pygame.K_RIGHT:
            # Move Ship to the Right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
            # Move Ship to the Right
                ship.moving_left = True

            elif event.key == pygame.K_SPACE:
                fire_bullet(ai_settings, screen, ship, bullets)
                

            elif event.key == pygame.K_q:
                
                
                pygame.mixer.music.stop()
                return True
            return False


def fire_bullet(ai_settings,screen,ship,bullets):

                #Create new bullet and add it to the bullet group
                if len(bullets) < ai_settings.bullets_allowed:
                    new_bullet = bullet.Bullet(ai_settings,screen,ship)
                    
                    bullets.add(new_bullet)
                    play_fire()
                    
def check_keyup_events(event,ship):

            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

        


def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    # Responds to key press and mouse event
    #Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           #sys.exit()
           #pygame.quit()
           pygame.mixer.music.stop()
           return True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
          


        elif event.type == pygame.KEYDOWN:
            return check_keydown_events(event, ai_settings, screen, ship, bullets)


        elif event.type == pygame.KEYUP:
           check_keyup_events(event,ship)

        return False


def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """start a new game when player click play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:

        #reset the game settings
        ai_settings.initialize_dynamic_settings()
        #Hiding the mouse cursor.
        pygame.mouse.set_visible(False)
        #reset the game statistics
        stats.reset_stats()
        stats.game_active = True

        #reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
            

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    
     #Redraw the screen during each pass through the loop.
     screen.fill(ai_settings.bg_color)

      #Redraw all bullets behind the ship and aliens
     for bullet in bullets.sprites():
         bullet.draw_bullet()
     
     ship.blitme()
#     alien.blitme()
     aliens.draw(screen)
     

     #Draw score information
     sb.show_score()

     #Draw the play button if the game is inactive
     if not stats.game_active:
         play_button.draw_button()

     #Make the most recently drawn screen visible.
     pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens, bullets):

    """Update the position of bullets and get rid of the old bullets"""
    #Update bullet position

    bullets.update()

        # Get rid of the bullets that have disappeared
    for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)



    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
    

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #check for any bullet that have hit aliens
    #If so,get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    

    if collisions:
     
        for aliens in collisions.values():
            play_collision()
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
        
    if len(aliens) == 0:
        # destroy exixting bullets and create new fleet,speed up game
        #If entirre fleet is destroyed, start a new level
       bullets.empty()
       ai_settings.increase_speed()

       #increase level
       stats.level +=1
       sb.prep_level()

       create_fleet(ai_settings, screen, ship, aliens)

 
def update_aliens(ai_settings,screen,stats,sb,ship, aliens,bullets):
     
    """Check is the fleet is on the edge,
    and then update the position of all alens in the fleet."""

    check_fleet_edges(ai_settings,aliens)

    aliens.update()

    #Look for ship alien collision
    if pygame.sprite.spritecollideany(ship,aliens):
        print("Ship hit!!!")
        
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
        

    #Look for the alien reaching the bottom of the screen
    check_aliens_bottom(ai_settings, screen,stats,sb, ship, aliens, bullets)


def create_fleet(ai_settings,screen,ship,aliens):

    """Create full fleet of alien"""


    alien = Alien.Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    

    #Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens, alien_number ,row_number)
        


def get_number_aliens_x(ai_settings, alien_width):

    """Detemine number of aliens that fit in the row"""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """Create an alien and place it in the row"""
    alien = Alien.Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.top = 40 + alien.rect.y
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2* alien_height))
    return number_rows


def check_fleet_edges(ai_settings,aliens):
    """Respond appropriately if aliens have reached the edge."""
    
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *=-1


def ship_hit(ai_settings,screen, stats, sb,ship,aliens, bullets):
    """Respond to ship being hit by bullets"""
    
    if stats.ships_left > 0:
        
        #Decrement ship left
        stats.ships_left -= 1

        #Update scoreboard
        sb.prep_ships()
 

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        #Pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, screen,stats,sb, ship, aliens, bullets):
    """check if any alien have reached bottom of the screen"""
    
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this game as if ship got the hit !!
            ship_hit(ai_settings,screen, stats, sb ,  ship,aliens, bullets)
            break

def check_high_score(stats,sb):
    """check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


