import time


def prime_count(n: int) -> int:
    """
    Counts the number of primes <= n using the Lucy Hedgehog algorithm.
    """
    if n < 2:
        return 0

    v = int(n**0.5)
    V: list[int] = []

    for i in range(1, v + 1):
        V.append(n // i)
    for i in range(V[-1] - 1, 0, -1):
        V.append(i)

    S = {i: i - 1 for i in V}

    for p in range(2, v + 1):
        if S[p] > S[p - 1]:
            sp = S[p - 1]
            p2 = p * p
            for v_i in V:
                if v_i < p2:
                    break
                S[v_i] -= S[v_i // p] - sp

    return S[n]


def S(n: int) -> int:
    """
    Calculates the sum of P(i, k) for a given maximum n.
    """
    if n < 2:
        return 0
    if n < 4:
        return prime_count(n)

    pi_n = prime_count(n)
    pi_n_minus_2 = prime_count(n - 2)
    m = n // 2

    term_1 = pi_n  # k = 1
    term_2 = m + pi_n_minus_2 - 2  # k = 2
    term_3 = (m - 2) * (n - m - 2)  # k >= 3

    return term_1 + term_2 + term_3


def solve_problem_543() -> int:
    # Generate Fibonacci sequence properly where F(0) = 0, F(1) = 1
    F = [0, 1]
    for _ in range(2, 45):  # We need up to F(44)
        F.append(F[-1] + F[-2])

    # Find the sum of all S(F(k)) over 3 <= k <= 44
    total_sum = 0
    for k in range(3, 45):
        total_sum += S(F[k])

    return total_sum


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_543()
    end = time.perf_counter()

    print(f"Result of problem 543 is {result}.")
    print(f"Finished in {end - begin} seconds.")
