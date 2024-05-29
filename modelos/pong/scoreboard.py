import pygame
from modelos.pong.display_config import DisplayConfig

class Scoreboard:
    def __init__(self) -> None:
        self._player1 = 0
        self._player2 = 0
        self._color = (0,0,255)
    
    def _config(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(f'{self._player1} vs {self._player2}', 
                           True, self._color)
        textRect = text.get_rect()
        textRect.center = (DisplayConfig.WIDTH // 2, 20)
        return [text, textRect]

    def draw(self, screen):
        text, textRect = self._config()[0], self._config()[1]
        screen.blit(text, textRect)

    def p1_goal(self):
        self._player1 += 1

    def p2_goal(self):
        self._player2 += 1