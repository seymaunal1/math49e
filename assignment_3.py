import time
from functools import lru_cache


def solve_problem_78_gemini() -> int:
    # p[n] will store p(n) % 1,000,000
    p: list[int] = [1]
    n: int = 0

    while True:
        n += 1

        p_n: int = 0
        k: int = 1

        while True:
            # Generalized pentagonal numbers for k and -k
            # g1 = k(3k-1)/2,  g2 = k(3k+1)/2
            g1: int = k * (3 * k - 1) // 2
            g2: int = k * (3 * k + 1) // 2

            # If the index is out of bounds, we stop the inner loop
            if g1 > n:
                break

            # The signs follow the pattern: +, +, -, -, +, +, -, -, ...
            # which is determined by (-1)^(k-1)
            sign: int = 1 if k % 2 == 1 else -1

            # Add p(n - g1)
            p_n += sign * p[n - g1]

            # Add p(n - g2) if within bounds
            if g2 <= n:
                p_n += sign * p[n - g2]

            k += 1

        # We only care about divisibility by 1,000,000
        p_n %= 1000000

        if p_n == 0:
            return n

        p.append(p_n)


# algorithm: this is called integer partition with partially ordered set. find the n that satisfy this equation
# p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7)..p(n - pentagonal_num)..


def pentagonal_numbers(n) -> list:
    nums = []
    if n == 1 or n == 0:
        nums.append(1)
        return nums
    k = 1
    while True:
        p1 = int(k * (3 * k - 1) / 2)
        p2 = int(k * (3 * k + 1) / 2)
        if p1 <= n:
            nums.append(p1)
        if p2 <= n:
            nums.append(p2)
        if p1 > n and p2 > n:
            break
        k += 1
    return nums


@lru_cache(maxsize=None)
def p(n) -> int:
    g = pentagonal_numbers(n)
    if n == 1 or n == 0:
        return 1
    if n < 0:
        return 0
    sum = 0
    for i in range(1, len(g) + 1):
        sum += (-1) ** ((i - 1) // 2) * p(n - g[i - 1])
    return sum


def solve_problem_78():
    n = 1
    divided_by = 1000000
    while True:
        n += 1
        if p(n) % divided_by == 0:
            print(n)
            break


if __name__ == "__main__":
    begin = time.perf_counter()
    result: int = solve_problem_78_gemini()
    end = time.perf_counter()

    print(f"Result of problem 78 is {result}.")
    print(f"Finished in {end - begin} seconds.")
