import math

from solutions.file_utils import InputType, read_input
from pydantic import BaseModel
from typing import Tuple, Callable, Optional
from functools import cmp_to_key


class Rule(BaseModel):
    before: int
    after: int


class PageNumberUpdate(BaseModel):
    pages: list[int]
    valid: Optional[bool] = None


def _get_input_data(input_type: InputType) -> Tuple[list[Rule], list[PageNumberUpdate]]:
    input_data = read_input(input_type=input_type, day="5a")
    rule_end_at = 0
    rules = []
    updates = []

    for index, line in enumerate(input_data):
        if line == "":
            rule_end_at = index
            break
        rule = [int(nr) for nr in line.split("|")]
        rules.append(Rule(before=rule[0], after=rule[1]))

    for update in input_data[rule_end_at + 1 :]:
        updates.append(
            PageNumberUpdate(pages=[int(update) for update in update.split(",")])
        )

    return rules, updates


def validate_updates(rules: list[Rule], updates: list[PageNumberUpdate]) -> None:
    for update in updates:
        corrected = sorted(update.pages, key=cmp_to_key(comparator(rules=rules)))
        update.valid = False if corrected != update.pages else True
        update.pages = corrected


def comparator(rules: list[Rule]) -> Callable:
    def _comparator(item1: int, item2: int) -> int:
        for rule in rules:
            if rule.before == item1 and rule.after == item2:
                return -1
        return 0

    return _comparator


def solve_a(input_type: InputType) -> int:
    rules, updates = _get_input_data(input_type=input_type)
    validate_updates(rules=rules, updates=updates)

    return sum(
        [
            update.pages[math.ceil((len(update.pages) - 1) / 2)]
            for update in updates
            if update.valid
        ]
    )


def solve_b(input_type: InputType) -> int:
    rules, updates = _get_input_data(input_type=input_type)
    validate_updates(rules=rules, updates=updates)

    return sum(
        [
            update.pages[math.ceil((len(update.pages) - 1) / 2)]
            for update in updates
            if not update.valid
        ]
    )
