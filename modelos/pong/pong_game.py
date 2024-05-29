import pygame
from modelos.pong.display_config import DisplayConfig
from modelos.pong.ball import Ball
from modelos.pong.player_1 import Player1
from modelos.pong.player_2 import Player2
from modelos.pong.scoreboard import Scoreboard
from modelos.pong.collision import Collision

class PongGame:
    def __init__(self) -> None:
        self._screen = pygame.display.set_mode((DisplayConfig.WIDTH, 
                                          DisplayConfig.HEIGHT))
        self._player_1 = Player1(DisplayConfig.WIDTH - DisplayConfig.WIDTH + 20,
                           DisplayConfig.HEIGHT/2)
        self._player_2 = Player2(DisplayConfig.WIDTH - 25,
                                  DisplayConfig.HEIGHT/2)
        self._score = Scoreboard()
        self._ball = Ball(DisplayConfig.WIDTH/2, DisplayConfig.HEIGHT/2,
                           self._screen)
        self._collision = Collision(self._player_1, self._player_2, self._ball, self._score)
    

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self._screen.fill(DisplayConfig.COLOR)
            self._score.draw(self._screen)
            self._player_1.draw(self._screen)
            self._player_2.draw(self._screen)
            self._ball.draw(self._screen)
            clock.tick(DisplayConfig.FPS)  # limits FPS to 60
            

            # Faz a movimentação dos players
            self._player_1.update()
            self._player_2.update()
            
            # Fazer a checagem das colisões
            self._collision.update()

            # flip() the display to put your work on screen
            # need att in the end of code! 
            pygame.display.flip()

    @staticmethod
    def rodar_o_jogo():
        pong = PongGame()
        pong.start()
