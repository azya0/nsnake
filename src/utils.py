from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum


@dataclass(frozen=True)
class Vector2D:
    x: int
    y: int

    def to_tuple(self) -> tuple[int, int]:
        return self.x, self.y

    def __floordiv__(self, value: int) -> Vector2D:
        return Vector2D(self.x // value, self.y // value)

    def __mul__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x * other.x, self.y * other.y)

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int) -> Vector2D:
        return Vector2D(self.x - other, self.y - other)
    
    def __le__(self, other: Vector2D) -> bool:
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other: Vector2D) -> bool:
        return self.x >= other.x and self.y >= other.y


@dataclass
class Node[T]:
    data: T

    next: Node[T] | None = None
    prev: Node[T] | None = None


class MoveDirection(IntEnum):
    Top = (0,)
    Left = (1,)
    Right = (2,)
    Down = (3,)
