import sys
import pygame
from Modules import bullet




def check_keydown_events(event,ai_settings,screen,ship,bullets):

            if event.key == pygame.K_RIGHT:
            # Move Ship to the Right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
            # Move Ship to the Right
                ship.moving_left = True

            elif event.key == pygame.K_SPACE:
                fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings,screen,ship,bullets):

                #Create new bullet and add it to the bullet group
                if len(bullets) < ai_settings.bullets_allowed:
                    new_bullet = bullet.Bullet(ai_settings,screen,ship)
                    bullets.add(new_bullet)

def check_keyup_events(event,ship):

            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

        


def check_events(ai_settings,screen,ship,bullets):
    # Responds to key press and mouse event
    #Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)


        elif event.type == pygame.KEYUP:
           check_keyup_events(event,ship)

        
            

def update_screen(ai_settings,screen,ship,bullets):
    
     #Redraw the screen during each pass through the loop.
     screen.fill(ai_settings.bg_color)

      #Redraw all bullets behind the ship and aliens
     for bullet in bullets.sprites():
         bullet.draw_bullet()
     
     ship.blitme()

     #Make the most recently drawn screen visible.
     pygame.display.flip()


def update_bullets(bullets):

    """Update the position of bullets and get rid of the old bullets"""
    #Update bullet position

    bullets.update()

        # Get rid of the bullets that have disappeared
    for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)

    
