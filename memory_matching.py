import sys
import pygame
import random
import pandas as pd
import numpy as np
from button_class import Button
from matching_cards_class import matching_cards

# initialze Pygame
pygame.init()

# these next 5 lines are for setting up the window
screenWidth = 1280
screenHeight = 720
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Memory Matching")
backgroundColor = (250, 223, 173)

## Button Images
buttonImage = pygame.image.load(r"Assets\bluebutton.png")
buttonImage = pygame.transform.scale(buttonImage,(300,100))
buttonSpacing = 0
buttonFont = 25
# these lines set up text font 
font_path = r"Assets\arcadeFont.ttf"
font_size = 24
font = pygame.font.Font(font_path, font_size)

# clock to use to track game time (fps usage)
clock = pygame.time.Clock()

## Testing Data with SP

# Function to filter rows based on the length of the second column
def filter_by_length(df, column_name, max_length):
    return df[df[column_name].str.len() <= max_length]

sp500 = pd.read_csv(r"Stock Data\s&p500_stocks.csv")
sp500 = sp500[["Symbol", "Security"]]
sp500 = filter_by_length(sp500, "Security", 15)
sp500Dict = dict(zip(sp500.Symbol, sp500.Security))



def play_matching(category, difficulty):
    """
    category is the set of cards used (dict of {symbol:name})
    difficulty: easy - 2x3, medium - 3x4, hard - 4X4
    """
    global buttonImage, buttonSpacing, buttonFont
    ## method to check if the two cards match:
    def is_matching(card1, card2):
        if card1 in category.keys():
            ##card 1 is ticker
            return category[card1] == card2
        elif card2 in category.keys():
            return category[card2] == card1
        
    ## method to flip all cards over after failed guess
    def makeAllFlipped(cards):
        for button in cards:
            if button.is_flipped == False:
                button.flip()

    ## draws text for the stop watch
    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect(center=(x, y))
        surface.blit(text_obj, text_rect)
            

    running = True
    start_time = pygame.time.get_ticks()

    ## Set Difficulty
    if difficulty == "easy":
        x,y = 3,2
        flip_time = 3000
        score = 180
        buttonImage = pygame.transform.scale(buttonImage,(500,166))
        buttonFont = 25
    elif difficulty == "medium":
        x,y = 4,3
        flip_time = 4000
        score = 240    
        buttonImage = pygame.transform.scale(buttonImage,(400,133))
        buttonFont = 20
    else:
        x,y = 5,4
        flip_time = 3000
        score = 300
        buttonImage = pygame.transform.scale(buttonImage,(300,100))
        buttonFont = 15

    ## Generate Card values
    stockPairs = []
    for i in range(x*y // 2):
          stockPairs.append(random.choice(list(category.items())))
    allItems = [item for t in stockPairs for item in t]
    random.shuffle(allItems)
    allCards = []
    

    ## Make Cards
    for i in range (1, x+1):
        for j in range(1, y+1):
            item = allItems[(i-1)*y + (j - 1)]
            if difficulty == "easy":
                x_pos = 343 + 593*(j-1)
                y_pos = 150 + 220*(i-1)
            elif difficulty == "medium":
                x_pos = 220 + 420*(j-1)
                y_pos = 140 + 160*(i-1)
            else:
                x_pos = 166 + 316*(j-1)
                y_pos = 140 + 130*(i-1)
            allCards.append(matching_cards(image=buttonImage, pos=(x_pos,y_pos), 
            text_input=item, font = pygame.font.Font(font_path, buttonFont), base_color="Black", hovering_color="White", back_image=buttonImage))
    
    #Flag for the initial flipping
    cards_flipped = False


    ## Count how many you have turned over
    count = 0
    cards = []

    #Stop Watch
    elapsed_time = 0
    stopwatch_running = False

    ## Win Screen
    winImage = pygame.image.load(r"Assets\stonks.jpg")
    homeButton = matching_cards(image=buttonImage, pos=(screenWidth//2, screenHeight*9//10), 
            text_input="Main Menu", font = pygame.font.Font(font_path, 30), base_color="Black", hovering_color="White", back_image=buttonImage)

    ## Running Loop
    while running:
        ## Captures Events
        for event in pygame.event.get():
            # handles game inputs
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in allCards:
                    if button.checkForInput(event.pos):
                        button.flip()
                        button.update(window)
                        count += 1
                        cards.append(button)
                        if count == 2:  # When two cards are clicked, start the delay
                            delay_start_time = pygame.time.get_ticks()
                # if homeButton.checkForInput(event.pos):
                #     pygame.quit()
                #     return
        
        window.fill(backgroundColor)

        ## Stop Watch
        current_time = pygame.time.get_ticks()
        if stopwatch_running:  # **Check if the stopwatch is running**
            elapsed_time = (current_time - start_time - flip_time) / 1000  # in seconds
        
        
        ## Win condition
        if len(allCards) == 0:
            stopwatch_running = False
            draw_text("Congrats!!!", pygame.font.Font(font_path, 40), "Red", x = screenWidth//2, y = screenHeight//2, surface = window)
            window.blit(winImage, (screenWidth//10, screenHeight//8))
            window.blit(winImage, (screenWidth*9//10 - winImage.get_width(), screenHeight//8))
            homeButton.update(window)

        draw_text(f"Time: {elapsed_time:.2f}s", font, "Black", window, screenWidth // 2, 30)  # **Display the elapsed time** 

        if not cards_flipped and current_time - start_time >= flip_time:
            for card in allCards:
                card.flip()  # Flip each card
            cards_flipped = True  # Set the flag to True so this only happens once
            stopwatch_running = True


        
        # After two cards are clicked, introduce a delay before the next action
        if count == 2 and current_time - delay_start_time >= 300:  # Wait for 500ms
            if is_matching(cards[0].text_input, cards[1].text_input):
                allCards.remove(cards[0])
                allCards.remove(cards[1])

            else:
                makeAllFlipped(allCards)
            count = 0
            cards = []
              
                        

        for button in allCards:
            button.update(window)
        
        pygame.display.flip()
        clock.tick(60)
    # quit Pygame if required
    pygame.quit()
    return 

play_matching(sp500Dict, "medium")