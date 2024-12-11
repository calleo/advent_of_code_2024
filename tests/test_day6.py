import pytest
from solutions.day6 import solve_a, solve_b
from solutions.file_utils import InputType


@pytest.mark.parametrize(
    "input_type, expected",
    [
        (InputType.SAMPLE, 41),
        (InputType.FULL, 4665),
    ],
)
def test_solve_a(input_type: InputType, expected: int):
    actual = solve_a(input_type=input_type)
    assert actual == expected


@pytest.mark.parametrize(
    "input_type, expected",
    [
        (InputType.SAMPLE, 6),
        (InputType.FULL, 1688),
    ],
)
def test_solve_b(input_type: InputType, expected: int):
    actual = solve_b(input_type=input_type)
    assert actual == expected
