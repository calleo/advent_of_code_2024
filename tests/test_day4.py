import pytest

from solutions.collections import Matrix
from solutions.file_utils import InputType
from solutions.day4 import solve_a, solve_b, solve_b_matrix


@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 18), (InputType.FULL, 2434)]
)
def test_solve_a(input_type: InputType, expected: int):
    actual = solve_a(input_type=input_type)
    assert actual == expected


@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 9), (InputType.FULL, 1835)]
)
def test_solve_b(input_type: InputType, expected: int):
    actual = solve_b(input_type=input_type)
    assert actual == expected


def test_solve_b_matrix():
    matrix = Matrix(
        matrix=[
            ["M", "A", "S"],
            ["M", "A", "S"],
            ["M", "A", "S"],
        ]
    )
    actual = solve_b_matrix(matrix=matrix)
    assert actual == 1
