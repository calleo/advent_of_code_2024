from solutions.file_utils import InputType, read_input
from collections import defaultdict


def _read_columns(day: str, input_type: InputType):
    rows = read_input(day=day, input_type=input_type)
    col1 = []
    col2 = []

    rows = map(
        lambda item: [int(i) for i in item if i != ""],
        map(lambda row: row.split(" "), rows),
    )
    for row in rows:
        col1.append(row[0])
        col2.append(row[-1])

    col1.sort()
    col2.sort()

    return col1, col2


def solve_a(input_type: InputType):
    col1, col2 = _read_columns(input_type=input_type, day="1a")
    answer = sum([abs(one - two) for one, two in zip(col1, col2)])
    return answer


def solve_b(input_type: InputType):
    occurrences = defaultdict(lambda: 0)
    col1, col2 = _read_columns(input_type=input_type, day="1a")

    for nr in col2:
        occurrences[nr] += 1

    return sum([nr * occurrences[nr] for nr in col1])
