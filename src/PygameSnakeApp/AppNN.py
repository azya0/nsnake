import pygame
import torch

from SnakeGame.Board import Board
from model import SnakeSolver, get_state_from_board, select_model_action
from utils import MoveDirection

from .App import SnakeGameApp


class SnakeGamePlayByNN(SnakeGameApp):
    def __init__(self, width, height, cells_x, cells_y, model_path: str):
        super().__init__(width, height, cells_x, cells_y)

        self.model = SnakeSolver(5)
        self.model.load_state_dict(torch.load(model_path))
        self.previous_apple_range: int | None = None
    
    def process_keydown(self, event) -> None:
        if event.key == pygame.K_r:
            self.board = Board(self.cells_x, self.cells_y)
    
    def do(self) -> None:
        state, self.previous_apple_range = get_state_from_board(self.board, self.previous_apple_range)

        action = select_model_action(self.model, state)

        self.board.move(MoveDirection(action))
