import pytest
from solutions.file_utils import InputType
from solutions.day3 import solve_a, _get_valid_instructions, solve_b


@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 161), (InputType.FULL, 160672468)]
)
def test_solve_a(input_type: InputType, expected: int):
    actual = solve_a(input_type=input_type)
    assert actual == expected


@pytest.mark.parametrize(
    "input_type, day, expected",
    [(InputType.SAMPLE, "3b", 48), (InputType.FULL, "3a", 84893551)],
)
def test_solve_b(input_type: InputType, day: str, expected: int):
    actual = solve_b(input_type=input_type, day=day)
    assert actual == expected


def test_get_valid_instructions():
    valid = _get_valid_instructions(
        instructions="xmul(2,4)%&mul[3,7]!@^do_not_mul"
        "(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )
    assert valid == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
