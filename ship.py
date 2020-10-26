import pygame

class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_left:
            self.rect.x -= 1
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)