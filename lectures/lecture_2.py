import time
from math import floor, isqrt, sqrt
from typing import Any

# Date: 23.02.2026


def continued_fraction() -> int:
    elements = [1]

    for _ in range(999):
        elements.append(2)

    numerators = [1, 3]
    denominators = [1, 2]

    for i in range(2, len(elements)):
        numerators.append(elements[i] * numerators[i - 1] + numerators[i - 2])
        denominators.append(elements[i] * denominators[i - 1] + denominators[i - 2])

    digit_counts_numerators = [len(str(abs(n))) for n in numerators]
    digit_counts_denominators = [len(str(abs(n))) for n in denominators]

    sum = 0
    for i in range(len(digit_counts_denominators)):
        if digit_counts_numerators[i] > digit_counts_denominators[i]:
            sum += 1

    return sum


def solve_problem_57() -> int:
    return continued_fraction()


# Last term of the period is equal to twice time of the initial term a_0
# Zero division error?
def solve_problem_64() -> int:
    counter: int = 0

    for N in range(3, 10000):
        F: int = floor(sqrt(N))
        a_0: int = F
        r: int = 0
        s: int = 1
        period: list[int] = [a_0]
        a: int = 1

        while a != 2 * a_0:
            # replace f = (floor(sqrt(N)) + r) // s
            f: int = (F + r) // s
            r, s = s * f - r, (N - (s * f - r) ** 2) // s
            a = (F + r) // s
            period.append(a)

        # if sqrt(N) is not int:
        if len(period) % 2 == 1:
            counter += 1
        # else:
        #     pass

    return counter


def solve_problem_64_chatgpt() -> int:
    counter: int = 0

    for N in range(2, 10000):
        F: int = isqrt(N)  # floor(sqrt(N))
        a_0: int = F

        if F * F == N:  # perfect square -> skip
            continue

        r: int = 0  # m
        s: int = 1  # d
        a: int = a_0  # a_k
        period_len: int = 0

        while True:
            r = s * a - r
            s = (N - r * r) // s
            a = (a_0 + r) // s
            period_len += 1

            if a == 2 * a_0:
                break

        if period_len % 2 == 1:
            counter += 1

    return counter


def solve_problem_64_gemini() -> int:
    odd_periods: int = 0

    for n in range(2, 10001):
        limit: int = int(isqrt(n))

        # Skip perfect squares to avoid zero division
        if limit * limit == n:
            continue

        # Initial values for the algorithm
        m: int = 0
        d: int = 1
        a: int = limit
        period_length: int = 0

        # The period ends when a = 2 * a_0
        while a != 2 * limit:
            m = d * a - m
            d = (n - m**2) // d
            a = (limit + m) // d
            period_length += 1

        if period_length % 2 == 1:
            odd_periods += 1

    return odd_periods


def solve_problem_104() -> Any:
    # TODO
    pass


if __name__ == "__main__":
    functions = [
        solve_problem_57,
        # solve_problem_64,
        solve_problem_64_chatgpt,
        solve_problem_64_gemini,
        # solve_problem_104,
    ]

    for index, function in enumerate(functions):
        begin = time.perf_counter()
        result: int = function()
        end = time.perf_counter()

        print(f"Result of {function.__name__} is {result}.")
        print(f"Finished in {end - begin} seconds.")

        if index < len(functions) - 1:
            print()
