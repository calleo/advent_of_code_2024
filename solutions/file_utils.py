from enum import StrEnum
import os

from solutions.collections import Matrix


class InputType(StrEnum):
    SAMPLE = "sample"
    FULL = "full"


def read_input(day: str, input_type: InputType) -> list[str]:
    lines = []
    path = (
        os.path.dirname(os.path.realpath(__file__))
        + "/input/"
        + f"day{day}_{input_type.value}.txt"
    )
    with open(path) as input_file:
        for line in input_file:
            lines.append(line.strip())
    return lines


def read_matrix(day: str, input_type: InputType) -> Matrix:
    lines = read_input(day=day, input_type=input_type)
    return Matrix(matrix=[list(line) for line in lines])
