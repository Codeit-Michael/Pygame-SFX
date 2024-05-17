import pygame, sys

from settings import WIDTH, HEIGHT
from world import World

pygame.init()

class Main:
	def __init__(self, screen):
		self.screen = screen
		self.FPS = pygame.time.Clock()

	def main(self):
		pygame.mixer.music.load("asset/sfx/bgm.wav")
		pygame.mixer.music.play(-1)

		world = World(self.screen)
		while True:
			self.screen.fill("black")

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			world.update()
			pygame.display.update()
			self.FPS.tick(30)


if __name__ == "__main__":
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	play = Main(screen)
	play.main()