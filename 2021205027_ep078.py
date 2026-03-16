import time
from functools import lru_cache

# Algorithm: this is called integer partition with partially ordered set. Find the n that satisfy this equation
# p(n) = p(n - 1) + p(n - 2) - p(n - 5) - p(n - 7)..p(n - gk)..


# First I want to calculate pentagonal numbers, I put them in a list every pentagonal numbers that I found.
# These are used in Euler's pentagonal number theorem for the partition function p(n).
def pentagonal_numbers(n: int) -> list[int]:
    nums: list[int] = []

    # For n = 0 or 1, the pentagonal number is 1.
    if n == 1 or n == 0:
        nums.append(1)
        return nums

    k = 1
    while True:
        # First pentagonal number calculation
        g1 = k * (3 * k - 1) // 2
        # Second pentagonal number calculation
        g2 = k * (3 * k + 1) // 2

        # Add values that do not exceed n.
        if g1 <= n:
            nums.append(g1)
        if g2 <= n:
            nums.append(g2)

        # Stop when it exceeds
        if g1 > n and g2 > n:
            break

        k += 1

    return nums


# I put the cache to increase the efficiency
# To find pentagonal numbers we have to create recursive function.
@lru_cache(maxsize=None)
def p(n: int) -> int:
    g = pentagonal_numbers(n)

    # Base cases:
    if n == 1 or n == 0:
        return 1
    if n < 0:
        return 0

    total = 0
    # p(n) = ∑(-1)**((i-1)//2) * p(n - g[i - 1]) for k starts from 1 to n - gk < 0
    # Signs follow the pattern: ++ -- ++ --
    for i in range(1, len(g) + 1):
        total += (-1) ** ((i - 1) // 2) * p(n - g[i - 1])

    return total


# Calculate the pentagonal numbers until first number is divisible by one million.
def solve_problem_78() -> int:
    n = 1
    divided_by = 1000000

    while True:
        n += 1

        if p(n) % divided_by == 0:
            return n


# Run the solve function
if __name__ == "__main__":
    begin = time.time()
    result: int = solve_problem_78()
    end = time.time()

    print(f"Result of problem 78 is {result}.")
    print(f"Finished in {end - begin} seconds.")
