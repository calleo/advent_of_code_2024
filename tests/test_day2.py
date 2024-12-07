import pytest
from solutions.file_utils import InputType
from solutions.day2 import solve_a, solve_b, _is_really_safe


@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 2), (InputType.FULL, 663)]
)
def test_solve_a(input_type: InputType, expected: int):
    actual = solve_a(input_type=input_type)
    assert actual == expected


# 736 is too high!
@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 4), (InputType.FULL, 692)]
)
def test_solve_b(input_type: InputType, expected: int):
    actual = solve_b(input_type=input_type)
    assert actual == expected


@pytest.mark.parametrize(
    "level,expected",
    [
        ([1, 2, 3, 4], True),
        ([4, 3, 2, 1], True),
        ([7, 3, 2, 1], True),
        ([10, 6, 2, 1], False),
        ([10, 6, 2, 4], False),
        ([10, 11, 8, 5], True),
    ],
)
def test_is_really_safe(level: list[int], expected: bool):
    actual = _is_really_safe(level=level)
    assert actual == expected
