from solutions.file_utils import InputType, read_matrix
from solutions.collections import Point, Matrix
from typing import Set

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"
OBSTRUCTION = "#"
EMPTY = "."


class InfiniteLoopError(Exception):
    def __init__(self, visited: Set[Point]):
        self.visited = visited


def find_start(matrix: Matrix) -> Point:
    for point in matrix.each_point():
        if point.value not in [OBSTRUCTION, EMPTY]:
            return point
    raise Exception("No start found")


def move(matrix: Matrix, point: Point, direction: str) -> Point:
    if direction == UP:
        return matrix.at(x=point.x, y=point.y + 1)
    elif direction == DOWN:
        return matrix.at(x=point.x, y=point.y - 1)
    elif direction == RIGHT:
        return matrix.at(x=point.x + 1, y=point.y)
    elif direction == LEFT:
        return matrix.at(x=point.x - 1, y=point.y)
    else:
        raise Exception("Invalid direction")


def new_direction(direction: str) -> str:
    if direction == UP:
        return RIGHT
    elif direction == RIGHT:
        return DOWN
    elif direction == DOWN:
        return LEFT
    elif direction == LEFT:
        return UP


def run_simulation(matrix: Matrix, start: Point):
    guard_pos = start
    direction = guard_pos.value
    visited = {guard_pos}
    infinite_loop_check = {guard_pos.directional_repr(direction=direction)}

    while True:
        peek = move(matrix=matrix, point=guard_pos, direction=direction)

        if peek.value == OBSTRUCTION:
            direction = new_direction(direction=direction)
        else:
            guard_pos = move(matrix=matrix, point=guard_pos, direction=direction)

            if guard_pos.value == "":
                # Guard has left the board
                break

            visited.add(guard_pos)
            repr = guard_pos.directional_repr(direction=direction)

            if repr in infinite_loop_check:
                raise InfiniteLoopError(visited=visited)

            infinite_loop_check.add(repr)

    return visited


def solve_a(input_type: InputType) -> int:
    matrix = read_matrix(input_type=input_type, day="6a")
    visited = run_simulation(matrix=matrix, start=find_start(matrix=matrix))
    return len(visited)


def solve_b(input_type: InputType) -> int:
    matrix = read_matrix(input_type=input_type, day="6a")
    start = find_start(matrix=matrix)

    visited = run_simulation(matrix=matrix, start=start)

    matrix.set(x=start.x, y=start.y, value=EMPTY)
    infinite_loops = 0

    for point in visited:
        if point == start:
            continue

        original_value = point.value
        matrix.set(x=point.x, y=point.y, value=OBSTRUCTION)

        try:
            run_simulation(matrix=matrix, start=start)
        except InfiniteLoopError:
            infinite_loops += 1

        matrix.set(x=point.x, y=point.y, value=original_value)

    return infinite_loops
