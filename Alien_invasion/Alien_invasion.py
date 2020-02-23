
import sys
import pygame
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
    ship = Ship.Ship(screen)
    

    #Start the main loop for the game.
    while True:

        gf.check_events()
        gf.update_screen(ai_settings,screen,ship)

       

run_game()