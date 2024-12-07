from enum import StrEnum
import os


class InputType(StrEnum):
    SAMPLE = "sample"
    FULL = "full"


def read_input(day: str, input_type: InputType):
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
