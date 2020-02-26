
import sys
import pygame
from pygame.sprite import Group
from Modules import settings 
from Modules import game_functions as gf
from Modules import Ship




def run_game():

    # initialized game and create a screen object
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alian Invation')

    #Make a ship
    ship = Ship.Ship(ai_settings,screen)
    #Make a group to store bullets in.
    bullets = Group()
    

    #Start the main loop for the game.
    while True:

        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)

       

run_game()