import sys
import pygame
import random
import pandas as pd
import numpy as np
from button_class import Button

class matching_cards():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, back_image = None):
		self.image = image
		self.back_image = back_image
		self.is_flipped = False
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		# If the card is flipped, show the front image; otherwise, show the back
		if self.is_flipped:
			screen.blit(self.image, self.rect)
		else:
			screen.blit(self.back_image, self.rect)  # Show back image when not flipped
			screen.blit(self.text, self.text_rect)  # If no back image, just render the text

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if not self.is_flipped:
			if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
				self.text = self.font.render(self.text_input, True, self.hovering_color)
			else:
				self.text = self.font.render(self.text_input, True, self.base_color)
						
	def flip(self):
		self.is_flipped = not self.is_flipped
		
        

