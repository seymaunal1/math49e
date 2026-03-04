import time


def solve_problem_78() -> int:
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


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_78()
    end = time.perf_counter()

    print(f"Result of problem 78 is {result}.")
    print(f"Finished in {end - begin} seconds.")
