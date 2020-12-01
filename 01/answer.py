import math
from itertools import combinations


def get_answer(numbers: list[int], combos: int = 2) -> int:
    result = [pair for pair in combinations(numbers, combos)
              if sum(pair) == 2020]

    multiplied = math.prod(result[0])

    print(f"The answer is {multiplied}")
    return multiplied

if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(item.strip()) for item in f.readlines()]
    get_answer(numbers, combos=3)