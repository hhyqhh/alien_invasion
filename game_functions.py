# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:44:12 2017

@author: hh
"""

import sys 
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
def update_screen(ai_settings,screen,ship):
    
     """更新屏幕上的图像，并切换到新屏幕"""
     # 每次循环时都重绘屏幕 
     screen.fill(ai_settings.bg_color)   
     ship.blitme() 

     # 让最近绘制的屏幕可见 
     pygame.display.flip() 
    