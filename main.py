import sys
import pygame
import random
import pandas as pd
import numpy as np
from button_class import Button


# initialze Pygame
pygame.init()

# these next 5 lines are for setting up the window
screenWidth = 1280
screenHeight = 720
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Stock Symbol Shenanigans")
backgroundColor = (250, 223, 173)


## Button Images
buttonImage = pygame.image.load("valorant.jpg")
buttonImage = pygame.transform.scale(buttonImage,(200,100))

# these lines set up text font 
font_path = "arcadeFont.ttf"
font_size = 24
font = pygame.font.Font(font_path, font_size)


# clock to use to track game time (fps usage)
clock = pygame.time.Clock()

def main_menu():
    running = True
    while running:
        # for background color
        window.fill(backgroundColor)

        # render the text
        TITLE_TEXT_COLOR = (78, 70, 55) 
        TITLE_TEXT = font.render("Capitol Connect", True, TITLE_TEXT_COLOR)

        # blit the text surface onto main display surface
        window.blit(TITLE_TEXT, (screenWidth // 2 - TITLE_TEXT.get_width() // 2, screenHeight // 2 - TITLE_TEXT.get_height() // 2))

        # update the display with new frame
        # pygame.display.flip()  
        
        # caps frame rate to 60 fps
        clock.tick(60) # should be at the end of the game loop

        ## Make Buttons
        
        OPTIONS_BUTTON = Button(image=buttonImage, pos=(screenWidth//3, screenHeight*3//4), 
                            text_input="OPTIONS", font = font, base_color="White", hovering_color="White")
        
        START_BUTTON = Button(image=buttonImage, pos=(screenWidth*2//3, screenHeight*3//4), 
                            text_input="START", font = font, base_color="White", hovering_color="White")

        
        for button in [OPTIONS_BUTTON, START_BUTTON]:
            button.update(window)
        
        ## Captures Events
        for event in pygame.event.get():
            # handles closing the game window
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    # quit Pygame if required
    pygame.quit()
    sys.exit()
print('skibidi')
main_menu()