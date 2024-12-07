from solutions.file_utils import InputType, read_input


def _read_levels_matrix(input_type: InputType) -> list[list[int]]:
    levels = read_input(input_type=input_type, day="2a")
    return [[int(nr) for nr in level.split(" ")] for level in levels]


def _is_safe(level: list[int]) -> bool:
    diffs = [a - b for a, b in zip(level, level[1:])]

    if not (all([diff > 0 for diff in diffs]) or all([diff < 0 for diff in diffs])):
        return False

    if any([abs(diff) > 3 for diff in diffs]):
        return False

    return True


def _is_really_safe(level: list[int]) -> bool:
    if _is_safe(level=level):
        return True

    for index in range(len(level)):
        if _is_safe(level=level[:index] + level[index + 1 :]):
            return True

    return False


def solve_a(input_type: InputType) -> int:
    levels = _read_levels_matrix(input_type=input_type)
    safe = [level for level in levels if _is_safe(level)]
    return len(safe)


def solve_b(input_type: InputType) -> int:
    levels = _read_levels_matrix(input_type=input_type)
    safe = [level for level in levels if _is_really_safe(level)]
    return len(safe)
