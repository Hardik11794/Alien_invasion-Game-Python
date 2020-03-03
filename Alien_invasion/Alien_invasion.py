
import sys
import pygame
from pygame.sprite import Group
from Modules import settings
from Modules import Alien
from Modules import game_functions as gf
from Modules import Ship
from Modules import game_stats
from Modules import scoreboard
from Modules import button






def run_game():

    # initialized game and create a screen object
    pygame.init()
    ai_settings = settings.Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alian Invasion')

    #Make the play button
    play_button =  button.Button(ai_settings, screen, "Play")
    #Create instance to store game statistics and create score board
    stats = game_stats.GameStats(ai_settings)
    sb = scoreboard.Scoreboard(ai_settings,screen,stats)
    #Make an alien
    alien = Alien.Alien( ai_settings, screen)
    #Make a ship
    ship = Ship.Ship(ai_settings,screen)
    #Make a group to store bullets and aliens in.
    bullets = Group()
    aliens = Group()

    #Create fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)
    

    #Start the main loop for the game.
    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
      

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

       

run_game()