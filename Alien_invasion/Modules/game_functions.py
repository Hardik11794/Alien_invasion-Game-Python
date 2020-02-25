import sys
import pygame


def check_events(ship):
    # Responds to key press and mouse event
    #Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            # Move Ship to the Right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
            # Move Ship to the Right
                ship.moving_left = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

        

        
            

def update_screen(ai_settings,screen,ship):
    
     #Redraw the screen during each pass through the loop.
     screen.fill(ai_settings.bg_color)
     ship.blitme()

     #Make the most recently drawn screen visible.
     pygame.display.flip()
     
