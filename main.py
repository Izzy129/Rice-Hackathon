import sys
import pygame
import random
import pandas as pd
import numpy as np

from button_class import Button
from main_menu import main_menu
from options import option_screen
from memory_matching import matching_cards

## Generates all data sets
allStockPairs = pd.read_csv(r"Stock Data/all_stock_info.csv")
allStockPairs = allStockPairs.drop("Exchange", axis = 1)

nyse = allStockPairs.tail(2717)

nasdaq = allStockPairs.head(3065)

djia = pd.read_csv(r"Stock Data\bluechip_DJIA.csv")
djia = djia[["Symbol", "Company"]]

houston = pd.read_csv(r"Stock Data\houston.csv")

popularTech = pd.read_csv(r"Stock Data\popular_tech.csv")

popular = pd.read_csv(r"Stock Data\popular.csv")

sp500 = pd.read_csv(r"Stock Data\s&p500_stocks.csv")
sp500 = sp500[["Symbol", "Security"]]

## Dictionaries for each set of stocks (symbol --> name)
allStockPairDicts = dict(zip(allStockPairs.Ticker, allStockPairs.Name))
nyseDict = dict(zip(nyse.Ticker, nyse.Name))
nasdaqDict = dict(zip(nasdaq.Ticker, nasdaq.Name))
djiaDict = dict(zip(djia.Symbol, djia.Company))
houstonDict = dict(zip(houston.Ticker, houston.Company))
popularTechDict = dict(zip(popularTech.Ticker, popularTech.Company))
popularDict = dict(zip(popular.Ticker, popular.Company))
sp500Dict = dict(zip(sp500.Symbol, sp500.Security))

# initialze Pygame
pygame.init()

# these next 5 lines are for setting up the window
screenWidth = 1280
screenHeight = 720
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Stock Symbol Shenanigans")
backgroundColor = (250, 223, 173)


## Button Images
buttonImage = pygame.image.load("bluebutton.png")
buttonImage = pygame.transform.scale(buttonImage,(200,100))

# these lines set up text font 
font_path = "arcadeFont.ttf"
font_size = 24
font = pygame.font.Font(font_path, font_size)


# clock to use to track game time (fps usage)
clock = pygame.time.Clock()

def main():
    running = True
    while running:
        # for background color
        window.fill(backgroundColor)

        main_menu()
        option_screen()
        matching_cards(sp500Dict, "easy")
        
        
        # update display with new frame
        pygame.display.update()
        clock.tick(60) # should be at the end of the game loop

    # quit Pygame if required
    pygame.quit()
    sys.exit()
