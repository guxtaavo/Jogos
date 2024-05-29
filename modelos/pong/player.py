import pygame
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y
        self._height = 70
        self._width = 5
        self._speed = 5
        self._color = 'white'

    @abstractmethod
    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, (self._x, self._y, self._width,
                                               self._height))