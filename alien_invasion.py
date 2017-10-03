# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:33:37 2017

@author: hh
"""
# import sys

import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats

import game_functions as gf

from button import Button
from scoreboard import Scoreboard 

def run_game():
    pygame.init()
    ai_settings = Settings()
    
    
    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")
      
    # 创建Play按钮 
    play_button = Button(ai_settings, screen, "Play Game")
    
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)    
    bullets = Group() 
    aliens = Group()
    
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    
    
     
    # 游戏主题循环
    while True:
    
        gf.check_events(ai_settings, screen, stats, play_button,ship,aliens,bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets) 
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets) 
            
        gf.update_screen(ai_settings, screen, stats, sb,ship,aliens,bullets,play_button)


run_game()




