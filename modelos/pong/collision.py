from modelos.pong.player_1 import Player1
from modelos.pong.player_2 import Player2
from modelos.pong.ball import Ball
from modelos.pong.display_config import DisplayConfig
from modelos.pong.scoreboard import Scoreboard

class Collision():
    def __init__(self, p1: Player1, p2: Player2, ball: Ball, score: Scoreboard) -> None:
        self._p1 = p1
        self._p2 = p2
        self._ball = ball
        self._score = score

    def update(self):
        # Update ball position based on speed
        self._ball._x += self._ball._speed_x
        self._ball._y += self._ball._speed_y

        # Check collision with the walls and adjust position and
        # speed accordingly
        # Collision with the left wall(Goal for Player 2)
        if self._ball._x < 0:
            self._ball.reset_ball()
            self._score._player2 += 1

        # Collision with the right wall (Goal for Player 1)
        if self._ball._x + self._ball._width > DisplayConfig.WIDTH:
            self._ball.reset_ball()
            self._score._player1 += 1

        
        # Collision with the top wall
        if self._ball._y < 0:
            self._ball._y = 0
            self._ball._speed_y = -self._ball._speed_y

        # Collision with the bottom wall
        if self._ball._y + self._ball._height > DisplayConfig.HEIGHT:
            self._ball._y = DisplayConfig.HEIGHT - self._ball._height
            self._ball._speed_y = -self._ball._speed_y

        # Check collision with player 1 paddle
        if (self._ball._x < self._p1._x + self._p1._width and 
            self._ball._y + self._ball._height > self._p1._y and 
            self._ball._y < self._p1._y + self._p1._height):
            self._ball._x = self._p1._x + self._p1._width
            self._ball._speed_x = -self._ball._speed_x

        # Check collision with player 2 paddle
        if (self._ball._x + self._ball._width > self._p2._x and 
            self._ball._y + self._ball._height > self._p2._y and 
            self._ball._y < self._p2._y + self._p2._height):
            self._ball._x = self._p2._x - self._ball._width
            self._ball._speed_x = -self._ball._speed_x