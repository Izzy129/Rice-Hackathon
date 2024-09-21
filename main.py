import sys
import pygame
import random
import pandas as pd
import numpy as np


# initialze Pygame
pygame.init()


# these next 5 lines are for setting up the window
screenWidth = 1280
screenHeight = 720
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Stock Symbol Shenanigans")
backgroundColor = (250, 223, 173)


# these lines set up text font 
font_path = "arcadeFont.ttf"
font_size = 24
font = pygame.font.Font(font_path, font_size)


# clock to use to track game time (fps usage)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        # handles closing the game window
        if event.type == pygame.QUIT:
            running = False
    # render the text
        
    TITLE_TEXT_COLOR = (78, 70, 55) 
    TITLE_TEXT = font.render("Stock Symbol Shenanigans", True, TITLE_TEXT_COLOR)
    
    
    # for background color
    window.fill(backgroundColor)

    # blit the text surface onto main display surface
    window.blit(TITLE_TEXT, (screenWidth // 2 - TITLE_TEXT.get_width() // 2, screenHeight // 2 - TITLE_TEXT.get_height() // 2))


    
    # update the display with new frame
    pygame.display.flip()  
    
    # caps frame rate to 60 fps
    clock.tick(60) # should be at the end of the game loop
    

# quit Pygame if required
pygame.quit()
sys.exit()

