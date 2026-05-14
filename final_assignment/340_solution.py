import time


def solve_problem_340() -> int:
    # Constants given in the problem
    a = 21**7
    b = 7**21
    c = 12**7
    MOD = 10**9

    # q and r such that b = q*a + r
    q, r = divmod(b, a)

    # Term 1: Sum of n from 0 to b
    # Formula: b*(b+1)/2
    s1 = (b * (b + 1) // 2) % MOD

    # Term 2: Sum of constant (4a - 4c) for (b+1) terms
    s2 = ((b + 1) * (4 * a - 4 * c)) % MOD

    # Term 3: (4a - 3c) * Sum_{k=0 to b} floor(k/a)
    # The sum of floor(k/a) from 0 to b=qa+r is:
    # a * (0 + 1 + ... + q-1) + (r+1) * q
    # = a * q * (q-1) / 2 + q * (r + 1)
    sum_floor = (a * q * (q - 1) // 2 + q * (r + 1)) % MOD
    s3 = ((4 * a - 3 * c) * sum_floor) % MOD

    # Result is the sum of all terms mod 10^9
    result = (s1 + s2 + s3) % MOD
    return result


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_340()
    end = time.perf_counter()

    print(f"Result of problem 347 is {result}.")
    print(f"Finished in {end - begin} seconds.")

    assert result == 291504964, "The result is wrong"
