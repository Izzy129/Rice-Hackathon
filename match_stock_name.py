import sys
import pygame
import random
import pandas as pd
import numpy as np
from button_class import Button


# sample dictionary for game
tech_companies = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com Inc.",
    "FB": "Meta Platforms Inc.",
    "TSLA": "Tesla Inc.",
    "NVDA": "NVIDIA Corporation",
    "ADBE": "Adobe Inc.",
    "NFLX": "Netflix Inc.",
    "INTC": "Intel Corporation",
    "CSCO": "Cisco Systems Inc.",
    "ORCL": "Oracle Corporation",
    "IBM": "International Business Machines Corporation",
    "CRM": "Salesforce.com Inc.",
    "PYPL": "PayPal Holdings Inc.",
    "AMD": "Advanced Micro Devices Inc.",
    "SQ": "Block Inc.",
    "UBER": "Uber Technologies Inc.",
    "LYFT": "Lyft Inc.",
    "SNAP": "Snap Inc.",
    "TWTR": "Twitter Inc.",
    "ZM": "Zoom Video Communications Inc.",
    "SHOP": "Shopify Inc.",
    "SPOT": "Spotify Technology S.A.",
    "DOCU": "DocuSign Inc."
}

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
# Create buttons in a 3x3 grid
button_width = 300
button_height = 150
button_spacing = 20
rows, cols = 3, 3
buttons = []


for i in range(rows):
    for j in range(cols):
        x = screenWidth // 4 * (j + 1)
        y = screenHeight // 4 * (i + 1)

        # select random company key from tech_companies dictionary
        company_symbol = random.choice(list(tech_companies.keys()))
        company_name = tech_companies[company_symbol]
        
        # remove key-value company
        del tech_companies[company_symbol]

        button_text = company_symbol
        buttons.append(Button(None, (x, y), button_text, button_font, BUTTON_TEXT_COLOR, BUTTON_HOVER_COLOR, BUTTON_BORDER_COLOR, 2))


def game():
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
                        print(f"Button {button.text_input} was clicked!")
        # end of event loop
        
        
        # for background color
        window.fill(backgroundColor)

    
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
game()