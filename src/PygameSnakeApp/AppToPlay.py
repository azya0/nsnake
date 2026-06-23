import pygame

from .App import SnakeGameApp
from utils import MoveDirection


class SnakeGamePlayByUser(SnakeGameApp):
    def process_keydown(self, event) -> None:
        match event.key:
            case pygame.K_a:
                self.board.move(MoveDirection.Left)
            case pygame.K_d:
                self.board.move(MoveDirection.Right)
            case pygame.K_w:
                self.board.move(MoveDirection.Top)
            case pygame.K_s:
                self.board.move(MoveDirection.Down)
    
    def do(self) -> None:
        return
