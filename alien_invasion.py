# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:33:37 2017

@author: hh
"""
# import sys

import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    
    
    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Aline Invasion")
    
    
    # 创建一个飞船
    ship = Ship(ai_settings,screen)

    # 游戏主题循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)


run_game()