from solutions.file_utils import InputType, read_input
import re


def _read_instructions(input_type: InputType, day: str) -> str:
    return "".join(read_input(input_type=input_type, day=day))


def _get_valid_instructions(instructions: str) -> list[str]:
    pattern = re.compile(r"(mul[(][0-9]{1,3},[0-9]{1,3}[)])")
    return pattern.findall(instructions)


def _calculate_instructions(instructions: list[str]) -> int:
    def multiply(instruction: str) -> int:
        instruction = (
            instruction.replace("mul", "").replace("(", "").replace(")", "").split(",")
        )
        return int(instruction[0]) * int(instruction[1])

    return sum([multiply(instruction) for instruction in instructions])


def solve_a(input_type: InputType) -> int:
    instructions = _read_instructions(input_type=input_type, day="3a")
    valid = _get_valid_instructions(instructions=instructions)
    return _calculate_instructions(instructions=valid)


def solve_b(input_type: InputType, day: str) -> int:
    instructions = "do()" + _read_instructions(input_type=input_type, day=day)
    pattern = re.compile(r"(do[(][)])|(don't[(][)])")
    instructions = [
        instruction for instruction in re.split(pattern, instructions) if instruction
    ]

    final_instructions = []
    prev = None
    for instruction in instructions:
        if prev:
            if prev == "do()":
                final_instructions.append(instruction)
        prev = instruction

    valid = _get_valid_instructions(instructions="".join(final_instructions))
    return _calculate_instructions(instructions=valid)
