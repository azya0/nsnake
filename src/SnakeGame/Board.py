from random import randint

from utils import Vector2D, MoveDirection, Node

from .Snake import Snake


class Board:
    def __init__(self, width: int, height: int) -> None:
        self._apple_position: Vector2D = Vector2D(0, 0)
        self._size: Vector2D = Vector2D(width, height)
        self._snake = Snake(self._size // 2)

        self.generate_apple()

    def generate_apple(self) -> None:
        already_selected: set[Vector2D] = set()

        head: Node[Vector2D] | None = self._snake.get_head()

        while head is not None:
            already_selected.add(head.data)
            head = head.prev

        while True:
            self._apple_position = Vector2D(
                randint(0, self._size.x - 1),
                randint(0, self._size.y - 1),
            )

            if self._apple_position not in already_selected:
                break

    def get_size(self) -> Vector2D:
        return self._size

    def move(self, direction: MoveDirection) -> None:
        self._snake.move(direction)

        if self._snake.get_head().data != self._apple_position:
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
