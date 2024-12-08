import pytest
from solutions.file_utils import InputType
from solutions.day5 import solve_a, solve_b


@pytest.mark.parametrize(
    "input_type, expected",
    [
        (InputType.SAMPLE, 143),
        (InputType.FULL, 6612),
    ],
)
def test_solve_a(input_type: InputType, expected: int):
    actual = solve_a(input_type=input_type)
    assert actual == expected


@pytest.mark.parametrize(
    "input_type, expected",
    [
        (InputType.SAMPLE, 123),
        (InputType.FULL, 4944),
    ],
)
def test_solve_b(input_type: InputType, expected: int):
    actual = solve_b(input_type=input_type)
    assert actual == expected
