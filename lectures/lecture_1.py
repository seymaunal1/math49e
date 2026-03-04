import operator
import timeit
from functools import reduce
from typing import Any, Callable, TypedDict

# import sys
# sys.setrecursionlimit(int(4e6))


class Problem(TypedDict):
    name: str
    function: Callable[[], Any]


def solve_problem_1() -> int:
    sum = 0

    for n in range(1, 999 + 1):
        if n % 3 == 0 or n % 5 == 0:
            sum += n

    return sum


def solve_problem_2a() -> list[int]:
    n = 4e6
    fibonacci = [1, 2]

    while True:
        new_fibonacci = fibonacci[-1] + fibonacci[-2]

        if new_fibonacci > n:
            break

        fibonacci.append(new_fibonacci)

    return fibonacci


def solve_problem_2b(fibonacci: list[int]) -> list[int]:
    # resolve with using recursive

    n = 4e6
    new_fibonacci = fibonacci[-1] + fibonacci[-2]

    if new_fibonacci > n:
        return fibonacci

    fibonacci.append(new_fibonacci)
    return solve_problem_2b(fibonacci)


def solve_problem_2c(fibonacci: list[int]) -> int:
    # assignment0: write a code for sum of fibonacci element for i = 3k+1 up to 4*10^6

    n = 4e6
    new_fibonacci = fibonacci[-1] + fibonacci[-2]

    if new_fibonacci > n:
        return reduce(
            operator.add, filter(lambda element: element % 2 == 0, fibonacci), 0
        )

    fibonacci.append(new_fibonacci)
    return solve_problem_2c(fibonacci)


def solve_problem_2d(old_fibonacci: int, fibonacci: int, sum: int) -> int:
    n = 4e6

    if old_fibonacci > n:
        return sum

    return solve_problem_2d(
        fibonacci,
        old_fibonacci + fibonacci,
        sum if old_fibonacci % 2 == 1 else sum + old_fibonacci,
    )


def solve_problem(name: str, function: Callable[[], Any]) -> None:
    print(f"Result of {name} is {function()}.")

    number_of_repetitions = 1000
    time = timeit.timeit(function, number=number_of_repetitions)
    print(f"{name} solved in {time} seconds.")


if __name__ == "__main__":
    problems: list[Problem] = [
        {"name": "Problem 1", "function": solve_problem_1},
        {"name": "Problem 2a", "function": solve_problem_2a},
        {"name": "Problem 2b", "function": lambda: solve_problem_2b([1, 2])},
        {"name": "Problem 2c", "function": lambda: solve_problem_2c([1, 2])},
        {"name": "Problem 2d", "function": lambda: solve_problem_2d(1, 2, 0)},
    ]

    for index, problem in enumerate(problems):
        solve_problem(problem["name"], problem["function"])

        if index < len(problems) - 1:
            print()
