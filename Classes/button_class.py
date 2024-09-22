import pygame
class Button():
	global unclicked_image
	unclicked_image = pygame.image.load(r"Assets\unclickedbutton.png")
	unclicked_image = pygame.transform.scale(unclicked_image, (300,100))
	
	global clicked_image
	clicked_image = pygame.image.load(r"Assets\clickedbutton.png")
	clicked_image = pygame.transform.scale(clicked_image, (300,100))


	def __init__(self, pos, text_input, font, base_color, hovering_color, size=(300,100)):
		self.image = unclicked_image
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
		self.width = size[0]
		self.height = size[1]
		self.clicked = False
		self.unclicked_image = unclicked_image
		self.clicked_image = clicked_image
  

  
	def update(self, screen):
		# debugging hitbox
		# pygame.draw.rect(screen, (255,0,0), self.rect, 5)
		if self.clicked:
			screen.blit(self.clicked_image, self.rect)
		else:
			screen.blit(self.unclicked_image, self.rect)
		screen.blit(self.text, self.text_rect)
		

	def checkForInput(self, position):
		#global clicked
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)