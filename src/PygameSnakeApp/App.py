from typing import Protocol, cast

import pygame

from SnakeGame.Board import Board
from utils import MoveDirection, Vector2D


class KeyboardEvent(Protocol):
    key: int


class SnakeGameApp:
    def __init__(self, width: int, height: int, cells_x: int, cells_y: int) -> None:
        self.board = Board(cells_x, cells_y)

        self._rect_size = Vector2D(width // cells_x, height // cells_y)

        self.fps: int = 120
        self._run: bool = True

        self.screen = pygame.display.set_mode((width, height))
        self.screen.set_alpha(None)

    def _rect_cords(self, coords: Vector2D) -> tuple[int, int, int, int]:
        return *(coords * self._rect_size).to_tuple(), *self._rect_size.to_tuple()

    def render(self) -> None:
        self.screen.fill((0, 0, 0))

        pygame.draw.rect(
            self.screen,
            pygame.Color(255, 0, 0),
            self._rect_cords(self.board.get_apple()),
        )

        for snake_position in self.board.get_snake():
            pygame.draw.rect(
                self.screen, pygame.Color(0, 255, 0), self._rect_cords(snake_position)
            )

        pygame.display.flip()

    def process_keydown(self, event: KeyboardEvent) -> None:
        match event.key:
            case pygame.K_a:
                self.board.move(MoveDirection.Left)
            case pygame.K_d:
                self.board.move(MoveDirection.Right)
            case pygame.K_w:
                self.board.move(MoveDirection.Top)
            case pygame.K_s:
                self.board.move(MoveDirection.Down)

    def event_processor(self, event: pygame.Event) -> None:
        match event.type:
            case pygame.QUIT:
                self._run = False
            case pygame.KEYDOWN:
                self.process_keydown(cast(KeyboardEvent, event))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()

        while (self._run and self.board.is_running()):
            for event in pygame.event.get():
                self.event_processor(event)

            self.render()

            clock.tick(self.fps)
