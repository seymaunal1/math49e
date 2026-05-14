import time


def solve_problem_659() -> int:
    N = 10_000_000
    LIMIT = 2 * N

    # Sieve to find primes up to LIMIT
    sieve = bytearray([1]) * (LIMIT + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(LIMIT**0.5) + 1):
        if sieve[i]:
            sieve[i * i : LIMIT + 1 : i] = bytearray([0]) * len(
                range(i * i, LIMIT + 1, i)
            )

    primes = [i for i in range(5, LIMIT + 1, 4) if sieve[i]]

    V = [4 * k * k + 1 for k in range(N + 1)]
    P = [0] * (N + 1)

    for p in primes:
        # Find a quadratic non-residue
        a = 2
        while pow(a, (p - 1) // 2, p) != p - 1:
            a += 1

        # Calculate modular square root of -1
        r = pow(a, (p - 1) // 4, p)

        # Calculate starting indices
        k1 = (r * ((p + 1) // 2)) % p
        k2 = p - k1

        # Sieve out the prime factor p from V[k]
        for k_start in (k1, k2):
            for k in range(k_start, N + 1, p):
                v = V[k]
                v //= p
                while v % p == 0:
                    v //= p
                V[k] = v
                P[k] = p

    ans = sum(max(P[k], V[k]) for k in range(1, N + 1))

    return ans % (10**18)


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_659()
    end = time.perf_counter()

    print(f"Result of problem 659 is {result}.")
    print(f"Finished in {end - begin} seconds.")

    assert result == 238518915714422000, "The result is wrong"
