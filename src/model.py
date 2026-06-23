from torch import nn, Tensor
import torch

from SnakeGame.Board import Board
from utils import Vector2D


class SnakeSolver(nn.Module):
    def __init__(self, square_side_size: int = 5, addition_params: int = 1) -> None:
        super().__init__()
        
        self.data = nn.Sequential(
            nn.Linear(square_side_size * square_side_size + addition_params, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 4)
        )
    
    def forward(self, input: Tensor) -> Tensor:
        return self.data(input)


def get_state_from_board(board: Board) -> torch.Tensor:
    def get_new_coords(current: Vector2D) -> tuple[int, int] | None:
        if abs(new_x := (current.x - result_center.x)) > 2 or abs(new_y := (current.y - result_center.y)) > 2:
            return None
        
        return new_x + 2, new_y + 2

    board_x, board_y = board.get_size().to_tuple()

    result = torch.zeros((5, 5), dtype=torch.float32)
    
    snake = board.get_snake()
    result_center = snake[0]
    result[2, 2] = 1.0

    for result_index_x, x_add in enumerate(range(-2, 3)):
        for result_index_y, y_add in enumerate(range(-2, 3)):
            if board_x > result_center.x + x_add >= 0 and board_y > result_center.y + y_add >= 0:
                continue

            result[result_index_x, result_index_y] = -1.0

    for snake_part in snake[1:]:
        if (new_coords := get_new_coords(snake_part)) is None:
            continue
        
        result[new_coords] = 1.0
    
    if (new_coords := get_new_coords((apple_position := board.get_apple()))) is None:
        return result
    
    result[new_coords] = 2.0

    apple_range: int = abs(result_center.x - apple_position.x) + abs(result_center.y - apple_position.y)

    return torch.cat((result.flatten(), torch.tensor([apple_range])))


def select_model_action(model: SnakeSolver, state: Tensor, dim: int = 0) -> int:
    with torch.no_grad():
        result: torch.Tensor = model(state)
        return int(result.argmax(dim=dim).item())
