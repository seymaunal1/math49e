import time


def solve_problem_347() -> int:
    N = 10_000_000

    # Step 1: Sieve of Eratosthenes to find primes up to N/2
    limit = N // 2
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    primes = [p for p, alive in enumerate(is_prime) if alive]

    # Step 2: Calculate M(p, q, N) for valid prime pairs
    found_m_values: set[int] = set()

    num_primes = len(primes)
    for i in range(num_primes):
        p = primes[i]
        # If p * (next prime) > N, no more pairs exist
        if i + 1 < num_primes and p * primes[i + 1] > N:
            break

        for j in range(i + 1, num_primes):
            q = primes[j]
            if p * q > N:
                break

            # Find largest p^a * q^b <= N with a, b >= 1
            max_val = 0
            pa = p
            while pa * q <= N:
                val = pa * q
                # Keep multiplying by q until we hit the limit N
                while val * q <= N:
                    val *= q
                if val > max_val:
                    max_val = val
                pa *= p

            if max_val > 0:
                found_m_values.add(max_val)

    return sum(found_m_values)


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_347()
    end = time.perf_counter()

    print(f"Result of problem 347 is {result}.")
    print(f"Finished in {end - begin} seconds.")

    assert result == 11109800204052, "The result is wrong"
