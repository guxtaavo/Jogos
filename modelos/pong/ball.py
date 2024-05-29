import pygame
from modelos.pong.display_config import DisplayConfig
import random

class Ball:

    def __init__(self, x, y, screen) -> None:
        self._x = x
        self._y = y
        self._color = 'blue'
        self._width = 30
        self._height = 30
        self._speed_x = 4
        self._speed_y = 4
        self._screen = screen
            
    def draw(self, screen):
        pygame.draw.rect(screen, self._color, (self._x, self._y, self._width,
                                                self._height))

    def reset_ball(self):
        self._x = (DisplayConfig.WIDTH - self._width) // 2
        self._y = (DisplayConfig.HEIGHT - self._height) // 2
        self._speed_x = random.choice([-4, 4])
        self._speed_y = random.choice([-4, 4])