import sys
import pygame
import random
import pandas as pd
import numpy as np
import random
from button_class import Button

# initialze Pygame
pygame.init()

# these next 5 lines are for setting up the window
screenWidth = 1280
screenHeight = 720
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Settings")
backgroundColor = (250, 223, 173)

# these lines set up text font 
font_path = "arcadeFont.ttf"
font_size = 24
smaller_font_size = 20
smaller_font = pygame.font.Font(font_path,smaller_font_size)
font = pygame.font.Font(font_path, font_size)
title_font = pygame.font.Font(font_path,35)


# clock to use to track game time (fps usage)
clock = pygame.time.Clock()

#These variables will be changed in Options and used in the Play function
difficulty = "Medium"
gamemode =  "Memory Match"
category = "All Stock"

all_buttons = []
difficulty_buttons = []
gamemode_buttons = []
category_buttons = []

# add difficulty buttons to difficulties list
easy_button = Button((200,screenHeight//2),"Easy",font,"Black","white")
difficulty_buttons.append(easy_button)

medium_button =Button((650,screenHeight//2),"Medium",font,"black","white")
difficulty_buttons.append(medium_button)

hard_button =Button((1100,screenHeight//2),"Hard",font,"black","white")
difficulty_buttons.append(hard_button)


# add gamemode buttons to gamemodes list
memory_match_button = Button((400,screenHeight//4),"Memory Match",smaller_font,"Black","white")
gamemode_buttons.append(memory_match_button)

guess_logo_button = Button((850,screenHeight//4),"Guess Logo",smaller_font,"Black","white")
gamemode_buttons.append(guess_logo_button)


# add category buttons to categories list
all_stock_button = Button((200,screenHeight - 200),"All Stock",font,"Black","white")
category_buttons.append(all_stock_button)

nyse_stock_button = Button((500,screenHeight-200),"NYSE",font,"Black","white")
category_buttons.append(nyse_stock_button)

nasdaq_stock_button = Button((800,screenHeight - 200),"Nasdaq",font,"Black","white")
category_buttons.append(nasdaq_stock_button)

dija_stock_button = Button((1100,screenHeight - 200),"DIJA",font,"Black","white")
category_buttons.append(dija_stock_button)

houston_stock_button = Button((200,screenHeight -100),"Houston",font,"Black","white")
category_buttons.append(houston_stock_button)

tech_stock_button = Button((500,screenHeight - 100),"Tech",font,"Black","white")
category_buttons.append(tech_stock_button)

pop_stock_button = Button((800,screenHeight - 100),"Popular",font,"Black","white")
category_buttons.append(pop_stock_button)

sp500_stock_button = Button((1100,screenHeight - 100),"S&P500",font,"Black","white")
category_buttons.append(sp500_stock_button)


all_buttons = []
all_buttons.extend(difficulty_buttons)
all_buttons.extend(gamemode_buttons)
all_buttons.extend(category_buttons)

def option_screen():
    global difficulty, gamemode, category
    
    pygame.display.set_caption("Options")
    running = True
    while running:
        for event in pygame.event.get():
            # handles closing the game window
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in all_buttons:
                    # first lets check if the current button we're looking at in the list was clicked
                    if button.checkForInput(event.pos):
                        # ok now we found the button that was clicked
                        # lets check which type of button it is and act accordingly
                        if button in gamemode_buttons:
                            # we only want one clicked button at a time
                                                        
                            # lets unclick all other buttons in gamemode buttons
                            for btn in gamemode_buttons:
                                btn.clicked = False
                            
                            # now lets click the current button
                            button.clicked = True
                            gamemode = button.text_input
                        if button in difficulty_buttons:
                            # we only want one clicked button at a time
                            
                            # lets unclick all other buttons in difficulty buttons
                            for btn in difficulty_buttons:
                                btn.clicked = False
                            
                            # now lets click the current button
                            button.clicked = True
                            difficulty = button.text_input
                        if button in category_buttons:
                            # we only want one clicked button at a time
                            
                            # lets unclick all other buttons in category buttons
                            for btn in category_buttons:
                                btn.clicked = False
                            
                            # now lets click the current button
                            button.clicked = True
                            
                            category = button.text_input

        window.fill(backgroundColor)
        title_text_color = (0,0,0)

        #Option Title Making
        opt_title_text = title_font.render("Options", True, title_text_color)
        window.blit(opt_title_text, (screenWidth//2 - opt_title_text.get_width()//2,10))

        #Difficulty Title Making
        difficulty_title_text = title_font.render("Difficulty", True, title_text_color)
        window.blit(difficulty_title_text,(screenWidth//2 - difficulty_title_text.get_width()//2, screenHeight//2 -100))

        #Gamemode Title Making
        gamemode_title_text = title_font.render("Gamemode", True, title_text_color)
        window.blit(gamemode_title_text,(screenWidth//2 - gamemode_title_text.get_width()//2, 70))

        #Category Title Making 
        category_title_text = title_font.render("Category", True, title_text_color)
        window.blit(category_title_text,(screenWidth//2 - category_title_text.get_width()//2, screenHeight - 300))
        
        #Draw buttons on window
        for button in all_buttons:
            button.update(window)
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    # sys.exit()
option_screen()
