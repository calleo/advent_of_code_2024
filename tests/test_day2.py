import pytest
from solutions.file_utils import InputType
from solutions.day2 import solve_a

@pytest.mark.parametrize(
    "input_type, expected", [(InputType.SAMPLE, 0), (InputType.FULL, 0)]
)
def test_solve_a(input_type: InputType, expected: int):
    actual = solve_a(input_type=input_type)
    assert actual == expected
