import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, size):
		super().__init__()
		self.x = pos[0]
		self.y = pos[1]
		self.rect = pygame.Rect(self.x, self.y, size, size)
		self.color = pygame.Color("red")

		# player status
		self.direction = pygame.math.Vector2(0, 0)
		self.lives = 5
		self.sound_move = False
	
		self.directions = {'left': (-8, 0), 'right': (8, 0), 'up': (0, -8), 'down': (0, 8)}
		self.keys = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}
		self.direction = (0, 0)

	def _action_sound(self):
		bling = pygame.mixer.Sound("asset/sfx/whoosh.mp3")
		pygame.mixer.Sound.play(bling)
		pygame.mixer.music.stop()

	def move(self, pressed_key):

		for key, key_value in self.keys.items():
			if pressed_key[key_value]:
				self.direction = self.directions[key]
				self.sound_move = True
				break
			else:
				self.direction = (0, 0)
				self.sound_move = False

		self.rect.move_ip(self.direction)
		

	def update(self, screen):
		if self.sound_move:
			self._action_sound()
			self.sound_move = False
		pygame.draw.rect(screen, self.color, self.rect)