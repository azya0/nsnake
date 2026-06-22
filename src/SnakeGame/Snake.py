from src.utils import Vector2D, MoveDirection, Node


class SnakeBodyCollision(BaseException):
    pass


class Snake:
    def __init__(self, position: Vector2D) -> None:
        self.head: Node[Vector2D] = Node[Vector2D](position)
        self.tail: Node[Vector2D] = self.head

        self.tail.next = self.head

        self.body: set[Vector2D] = set()
        self.body.add(self.head.data)

    def _update_position(self, direction_vector: Vector2D) -> None:
        new_head_position: Vector2D = self.head.data + direction_vector

        if new_head_position in self.body:
            raise SnakeBodyCollision

        new_head: Node[Vector2D] = Node[Vector2D](new_head_position)

        new_head.prev = self.head
        self.head.next = new_head

        self.head = new_head

        self.body.add(new_head.data)

    def get_head(self) -> Node[Vector2D]:
        return self.head

    def remove_tail(self) -> None:
        assert self.tail.next is not None
        
        self.body.remove(self.tail.data)

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
