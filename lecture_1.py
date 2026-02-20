import operator
import timeit
from functools import reduce

# import sys
# sys.setrecursionlimit(int(4e6))


def problem_1() -> int:
    sum = 0

    for n in range(1, 999 + 1):
        if n % 3 == 0 or n % 5 == 0:
            sum += n

    return sum


def problem_2a() -> list[int]:
    n = 4e6
    fibonacci = [1, 2]

    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    return fibonacci


def problem_2b(fibonacci: list[int]) -> list[int]:
    # resolve with using recursive

    n = 4e6
    new_fibonacci = fibonacci[-1] + fibonacci[-2]

    if new_fibonacci > n:
        return fibonacci

    fibonacci.append(new_fibonacci)
    return problem_2b(fibonacci)


def problem_2c(fibonacci: list[int]) -> int:
    # assignment0: write a code for sum of fibonacci element for i = 3k+1 up to 4*10^6

    n = 4e6
    new_fibonacci = fibonacci[-1] + fibonacci[-2]

    if new_fibonacci > n:
        return reduce(
            operator.add, filter(lambda element: element % 2 == 0, fibonacci), 0
        )

    fibonacci.append(new_fibonacci)
    return problem_2c(fibonacci)


def problem_2d(old_fibonacci: int, fibonacci: int, sum: int) -> int:
    n = 4e6

    if old_fibonacci > n:
        return sum

    return problem_2d(
        fibonacci,
        old_fibonacci + fibonacci,
        sum if old_fibonacci % 2 == 1 else sum + old_fibonacci,
    )


if __name__ == "__main__":
    number_of_repetitions = 1000

    time_1 = timeit.timeit(problem_1, number=number_of_repetitions)
    time_2a = timeit.timeit(problem_2a, number=number_of_repetitions)
    time_2b = timeit.timeit(lambda: problem_2b([1, 2]), number=number_of_repetitions)
    time_2c = timeit.timeit(lambda: problem_2c([1, 2]), number=number_of_repetitions)
    time_2d = timeit.timeit(lambda: problem_2d(1, 2, 0), number=number_of_repetitions)

    print(f"Problem 1 finished in {time_1} seconds.")
    print(f"Problem 2a finished in {time_2a} seconds.")
    print(f"Problem 2b finished in {time_2b} seconds.")
    print(f"Problem 2c finished in {time_2c} seconds.")
    print(f"Problem 2d finished in {time_2d} seconds.")

    print("Sum 2c:", problem_2c([1, 2]))
    print("Sum 2d:", problem_2d(1, 2, 0))
