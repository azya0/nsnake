from enum import IntEnum
from random import randint

from src.utils import Vector2D, MoveDirection, Node

from .Snake import Snake, SnakeBodyCollision


class BoardStatus(IntEnum):
    RUNNING = 0,
    LOSE = 1,
    WIN = 2,


class BoardException(BaseException):
    pass


class Board:
    def __init__(self, width: int, height: int) -> None:
        self._apple_position: Vector2D = Vector2D(0, 0)
        self._size: Vector2D = Vector2D(width, height)
        self._snake = Snake(self._size // 2)
        self._status = BoardStatus.RUNNING

        self.generate_apple()

    def generate_apple(self) -> None:
        already_selected: set[Vector2D] = set()

        head: Node[Vector2D] | None = self._snake.get_head()

        while head is not None:
            already_selected.add(head.data)
            head = head.prev
        
        if len(already_selected) == self._size.x * self._size.y:
            self._status = BoardStatus.WIN
            return

        while True:
            self._apple_position = Vector2D(
                randint(0, self._size.x - 1),
                randint(0, self._size.y - 1),
            )

            if self._apple_position not in already_selected:
                break
    
    def is_running(self) -> None:
        return self._status == BoardStatus.RUNNING

    def get_status(self) -> BoardStatus:
        return self._status

    def get_size(self) -> Vector2D:
        return self._size

    def is_inner(self, head_position: Vector2D) -> bool:
        return Vector2D(0, 0) <= head_position <= self._size - 1

    def move(self, direction: MoveDirection) -> None:
        if not self.is_running():
            raise BoardException
        
        try:
            self._snake.move(direction)
        except SnakeBodyCollision:
            self._status = BoardStatus.LOSE
            return

        head_position = self._snake.get_head().data
        
        if not self.is_inner(head_position):
            self._status = BoardStatus.LOSE
            return

        if head_position != self._apple_position:
            self._snake.remove_tail()
            return

        self.generate_apple()

    def get_snake(self) -> list[Vector2D]:
        result: list[Vector2D] = []

        head: Node[Vector2D] | None = self._snake.get_head()

        while head is not None:
            result.append(head.data)
            head = head.prev

        return result

    def get_apple(self) -> Vector2D:
        return self._apple_position
