import pygame
from player import Player
from settings import HEIGHT, WIDTH, player_size

class World:
	def __init__(self, screen):
		self.screen = screen
		self.game_over = False
		self.player_speed = 3
		self.color = pygame.Color("indigo")
		self._generate_world()

	# create and add player to the screen
	def _generate_world(self):
		player_x, player_y = WIDTH // 2, HEIGHT // 2
		center_size = player_size // 2
		self.player = Player((player_x - center_size, player_y - center_size), player_size)

	def update(self):
		keys = pygame.key.get_pressed()
		self.player.move(keys)

		self.player.update(self.screen)