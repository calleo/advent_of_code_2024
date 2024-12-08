from solutions.file_utils import InputType, read_matrix
from solutions.collections import Point, Matrix

import re


def solve_a(input_type: InputType) -> int:
    matches = 0
    pattern = re.compile(r"XMAS")
    matrix = read_matrix(input_type=input_type, day="4a")

    all_texts = (
        matrix.all_cols_as_str()
        + [col[::-1] for col in matrix.all_cols_as_str()]
        + matrix.all_rows_as_str()
        + [col[::-1] for col in matrix.all_rows_as_str()]
        + matrix.all_diagonals_as_str()
        + [col[::-1] for col in matrix.all_diagonals_as_str()]
    )

    for text in all_texts:
        matches += len(re.findall(pattern, text))

    return matches


def _is_xmas_point(point: Point, matrix: Matrix) -> bool:
    words = ["MAS", "SAM"]
    sw_to_ne = [
        point.value,
        matrix.at(x=point.x + 1, y=point.y + 1).value or "",
        matrix.at(x=point.x + 2, y=point.y + 2).value or "",
    ]
    se_to_nw = [
        matrix.at(x=point.x + 2, y=point.y).value or "",
        matrix.at(x=point.x + 1, y=point.y + 1).value or "",
        matrix.at(x=point.x, y=point.y + 2).value or "",
    ]

    return "".join(sw_to_ne) in words and "".join(se_to_nw) in words


def solve_b(input_type: InputType) -> int:
    matrix = read_matrix(input_type=input_type, day="4a")
    return solve_b_matrix(matrix=matrix)


def solve_b_matrix(matrix: Matrix) -> int:
    xmas_points = 0

    for point in matrix.each_point():
        if _is_xmas_point(point=point, matrix=matrix):
            xmas_points += 1
            _is_xmas_point(point=point, matrix=matrix)

    return xmas_points
