from utils import Vector2D, MoveDirection, Node


class Snake:
    def __init__(self, position: Vector2D) -> None:
        self.head: Node[Vector2D] = Node[Vector2D](position)
        self.tail: Node[Vector2D] = self.head

        self.tail.next = self.head

    def _update_position(self, direction_vector: Vector2D) -> None:
        new_head: Node[Vector2D] = Node[Vector2D](self.head.data + direction_vector)

        new_head.prev = self.head
        self.head.next = new_head

        self.head = new_head

    def get_head(self) -> Node[Vector2D]:
        return self.head

    def remove_tail(self) -> None:
        assert self.tail.next is not None

        self.tail = self.tail.next
        self.tail.prev = None

    def move(self, direction: MoveDirection) -> None:
        match direction:
            case MoveDirection.Top:
                direction_vector = Vector2D(0, -1)
            case MoveDirection.Left:
                direction_vector = Vector2D(-1, 0)
            case MoveDirection.Right:
                direction_vector = Vector2D(1, 0)
            case MoveDirection.Down:
                direction_vector = Vector2D(0, 1)

        self._update_position(direction_vector)
