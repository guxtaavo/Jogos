import pygame
from modelos.pong.player import Player
from modelos.pong.display_config import DisplayConfig

class Player1(Player):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if (self._y - self._speed) > 0:
                self._y -= self._speed
        if keys[pygame.K_s]:
            if (self._y + self._speed + self._height) < DisplayConfig.HEIGHT:
                self._y  += self._speed
