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
pygame.display.set_caption("Capital Connect")

# Colors
backgroundColor = (250, 223, 173)
TITLE_TEXT_COLOR = (78, 70, 55)
BUTTON_COLOR = (246, 134, 189)
BUTTON_HOVER_COLOR = (170, 170, 170)
BUTTON_TEXT_COLOR = (78, 70, 55)
BUTTON_BORDER_COLOR = (42, 42, 42)  # Jett color


# these lines set up text font 
font_path = "arcadeFont.ttf"
title_font = pygame.font.Font(font_path, 48) # size 48 font 
button_font = pygame.font.Font(font_path, 24) # size 24 font

# clock to use to track game time (fps usage)
clock = pygame.time.Clock()

# let make a list for the buttons
# storing them in here allows us to detect if they were pressed later in event handling
buttons = []

                     #image, (x_coord, y_coord),                       text,       font,      base_color,       hovering_color
start_button = Button((screenWidth // 4, screenHeight * 3 // 4), "Start", button_font, BUTTON_TEXT_COLOR, BUTTON_HOVER_COLOR)
buttons.append(start_button)

                     #image,           (x_coord, y_coord),                  text,       font,      base_color,       hovering_color
options_button = Button((screenWidth // 2, screenHeight * 3 // 4), "Options", button_font, BUTTON_TEXT_COLOR, BUTTON_HOVER_COLOR)
buttons.append(options_button)

                     #image,           (x_coord, y_coord),                  text,       font,      base_color,       hovering_color
quit_button = Button((screenWidth * 3 // 4, screenHeight * 3 // 4 ), "Quit", button_font, BUTTON_TEXT_COLOR, BUTTON_HOVER_COLOR)
buttons.append(quit_button)

def main_menu():
    running = True
    while running:
        # captures pygame events
        for event in pygame.event.get():
            # handles closing the game window
            if event.type == pygame.QUIT:
                running = False
                
            # handles button clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # lets loop through all buttons to find which one was clicked
                for button in buttons:
                    # check if the mouse click was within the button's rectangle
                    # this code is from the button class
                    if button.checkForInput(event.pos):
                        # to change the color of the button when clicked
                        button.clicked = not button.clicked
                        # rn im using the button text to determine which button was clicked, probably should change later
                        if button.text_input == "Start":
                            print("Start Game button clicked")
                        elif button.text_input == "Options":
                            print("Options button clicked")
                        elif button.text_input == "Quit":
                            running = False 
        # end of event loop
        
        
        # for background color
        window.fill(backgroundColor)

        # render the title 
        TITLE_TEXT = title_font.render("Capital Connect", True, TITLE_TEXT_COLOR)

        # blit the title onto main display surface
        window.blit(TITLE_TEXT, (screenWidth // 2 - TITLE_TEXT.get_width() // 2, screenHeight // 4 - TITLE_TEXT.get_height() // 2))

        # draw buttons on window
        for button in buttons:
            # this method from class already blits button to screen, don't blit buttons in main loop
            button.update(window)
    

        # DEBUGGING: draw lines to show half and quarter marks of the screen
        pygame.draw.line(window, (0, 0, 0), (0, screenHeight // 2), (screenWidth, screenHeight // 2), 1)
        pygame.draw.line(window, (0, 0, 0), (0, screenHeight // 4), (screenWidth, screenHeight // 4), 1)
        pygame.draw.line(window, (0, 0, 0), (0, screenHeight * 3 // 4), (screenWidth, screenHeight * 3 // 4), 1)
        pygame.draw.line(window, (0, 0, 0), (screenWidth // 2, 0), (screenWidth // 2, screenHeight), 1)
        pygame.draw.line(window, (0, 0, 0), (screenWidth // 4, 0), (screenWidth // 4, screenHeight), 1)
        pygame.draw.line(window, (0, 0, 0), (screenWidth * 3 // 4, 0), (screenWidth * 3 // 4, screenHeight), 1)
        # END DEBUGGING
        
        
                
        # update display with new frame
        pygame.display.flip()
        
        # caps frame rate to 60 fps
        clock.tick(60) # should be at the end of the game loop
    # quit Pygame if required
    pygame.quit()
    sys.exit()
main_menu()