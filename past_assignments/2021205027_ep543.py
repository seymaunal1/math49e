# Problem 543:
import time


def prime_count(n: int) -> int:
    """
    Computes π(n): the number of primes <= n.

    This is a function that is written with Lucy Hedgehog algorithm to find the number of prime numbers up to n.
    """
    if n < 2:
        return 0
    # the limit is the root of v
    v = int(n**0.5)
    V: list[int] = []
    # make a compressed list of values n//i to enable fast prime counting
    for i in range(1, v + 1):
        V.append(n // i)
    for i in range(V[-1] - 1, 0, -1):
        V.append(i)
    # s is the dictionary of the multipliers of n
    S = {i: i - 1 for i in V}
    # the filter to get the prime numbers
    for p in range(2, v + 1):
        # If S[p] > S[p-1], then p is prime
        if S[p] > S[p - 1]:
            sp = S[p - 1]
            p2 = p * p
            # Remove contributions of multiples of p using inclusion-exclusion principle
            for v_i in V:
                if v_i < p2:
                    break
                S[v_i] -= S[v_i // p] - sp

    return S[n]


def S(n: int) -> int:
    if n < 2:
        return 0
    if n < 4:
        return prime_count(n)
    # calculates the number of prime numbers up to n
    pi_n = prime_count(n)
    # calculates the number of prime numbers up to n - 2
    pi_n_minus_2 = prime_count(n - 2)

    # the elements that hold k = 1 up to n i.e. only prime numbers can hold k = 1
    part_1 = pi_n
    # Count numbers with k = 2:
    # - all even numbers
    # - odd numbers n such that n-2 is prime
    part_2 = (n // 2) + pi_n_minus_2 - 2

    if n <= 5:
        return part_1 + part_2
    # Count contributions for k >= 3 using a closed-form expression derived from the problem
    part_3 = (n // 2 - 2) * (n + 1) - (n // 2) * (n // 2 + 1) + 6

    return part_1 + part_2 + part_3


def solve_problem_543() -> int:
    # Generate Fibonacci sequence  where F(0) = 0, F(1) = 1
    F = [0, 1]
    for _ in range(2, 45):  # We need up to F(44)
        F.append(F[-1] + F[-2])

    # Find the sum of all S(F(k)) over 3 <= k <= 44
    total_sum = 0
    for k in range(3, 45):
        total_sum += S(F[k])
    return total_sum


if __name__ == "__main__":
    begin = time.time()
    result = solve_problem_543()
    end = time.time()

    print(f"Result of problem 543 is {result}.")
    print(f"Finished in {end - begin} seconds.")
