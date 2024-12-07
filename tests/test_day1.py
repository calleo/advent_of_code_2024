import pytest

from solutions.day1 import solve_a, solve_b
from solutions.file_utils import InputType


@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 11), (InputType.FULL, 1666427)]
)
def test_solve_a(input_type: InputType, expected: int):
    actual = solve_a(input_type=input_type)
    assert actual == expected


@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 31), (InputType.FULL, 24316233)]
)
def test_solve_b(input_type: InputType, expected: int):
    actual = solve_b(input_type=input_type)
    assert actual == expected
