import itertools
import logging

import pytest

from SnakeGame.Board import Board, BoardStatus
from utils import MoveDirection


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@pytest.fixture
def board() -> Board:
    return Board(5, 6)


def goto_zero(game: Board, steps: int) -> None:
    for _ in range(steps):
        game.move(MoveDirection.Left)
        game.move(MoveDirection.Top)


def test_game_winnable(board: Board) -> None:
    def cycle_moves_from_2_3() -> list[MoveDirection]:
        return [
            MoveDirection.Left,
            MoveDirection.Down,
            MoveDirection.Right,
            MoveDirection.Right,
            MoveDirection.Right,
            MoveDirection.Down,
            MoveDirection.Left,
            MoveDirection.Left,
            MoveDirection.Left,
            MoveDirection.Left,
            MoveDirection.Top,
            MoveDirection.Top,
            MoveDirection.Top,
            MoveDirection.Top,
            MoveDirection.Top,
            MoveDirection.Right,
            MoveDirection.Right,
            MoveDirection.Right,
            MoveDirection.Right,
            MoveDirection.Down,
            MoveDirection.Left,
            MoveDirection.Left,
            MoveDirection.Left,
            MoveDirection.Down,
            MoveDirection.Right,
            MoveDirection.Right,
            MoveDirection.Right,
            MoveDirection.Down,
            MoveDirection.Left,
            MoveDirection.Left,
        ]
    
    snake_size: int = 0

    for move in itertools.cycle(cycle_moves_from_2_3()):
        if (new_size := len(board.get_snake())) != snake_size:
            snake_size = new_size
            logger.info(f"{new_size}/30")

        board.move(move)

        if (not board.is_running()):
            break
    
    assert board._status == BoardStatus.WIN
