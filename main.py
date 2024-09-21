import sys
import pygame
import random
import pandas as pd
import numpy as np

## Initializes all stock data
# All stocks
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
screenWidth = 1280
screenHeight = 720


## Initializes all data
# All stocks
# allStockPairs = pd.read_csv(r'/Stock Data/all_stock_info.csv')
# print(allStockPairs)

# initialze Pygame
pygame.init()

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Stock Symbol Shenanigans")

# peach color
backgroundColor = (250, 223, 173)

# clock to use to track game time (fps usage)
clock = pygame.time.Clock()
running = True


# font for text throughout game
font_path = "arcadeFont.ttf"
font_size = 24
font = pygame.font.Font(font_path, font_size)

while running:
    for event in pygame.event.get():
        # handles closing the game window
        if event.type == pygame.QUIT:
            running = False
    # render the text
    
    TITLE_TEXT_COLOR = (78, 70, 55) 
    TITLE_TEXT = font.render("Stock Symbol Shenanigans", True, TITLE_TEXT_COLOR)
    

    # for background color
    win.fill(backgroundColor)

    # blit the text surface onto main display surface
    win.blit(TITLE_TEXT, (screenWidth // 2 - TITLE_TEXT.get_width() // 2, screenHeight // 2 - TITLE_TEXT.get_height() // 2))


    
    # update the display with new frame
    pygame.display.flip()  
    
    # caps frame rate to 60 fps
    clock.tick(60) # should be at the end of the game loop
    
    
# quit Pygame if required
pygame.quit()
sys.exit()