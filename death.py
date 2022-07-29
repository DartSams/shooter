import pygame


class Death(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 15):
			img = pygame.image.load(rf"ghost-pack\PNG\Wraith_03\PNG Sequences\Dying\Wraith_03_Dying_{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self): #cycles through the death animation
		death_speed = 4 
		self.counter += 1

		if self.counter >= death_speed and self.index < len(self.images) - 1: #resets animation to get ready for next kill
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= death_speed: #deletes the current death animation from screen can deactivate function for graveyard effect
			self.kill()