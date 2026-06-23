from abc import ABC, abstractmethod

from typing import Protocol, cast

import pygame

from SnakeGame.Board import Board
from utils import Vector2D


class KeyboardEvent(Protocol):
    key: int


class SnakeGameApp(ABC):
    def __init__(self, width: int, height: int, cells_x: int, cells_y: int) -> None:
        self.cells_x = cells_x
        self.cells_y = cells_y
        self.board = Board(cells_x, cells_y)

        self._rect_size = Vector2D(width // cells_x, height // cells_y)

        self.fps: int = 10
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

    @abstractmethod
    def process_keydown(self, event: KeyboardEvent) -> None:
        pass
    
    @abstractmethod
    def do(self) -> None:
        pass

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

            self.do()
            self.render()

            clock.tick(self.fps)
