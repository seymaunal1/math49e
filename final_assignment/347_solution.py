# problem 347/level 5

import time

limit = 10_000_000


# First find the all prime numbers up to limit with sieve function
def sieve(limit):
    """
    This is well known algorithm to find all the prime numbers up to the limit.
    It returns a list of prime numbers.
    """
    is_prime = [True] * (limit + 1)
    # skip 0 and 1
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # If p is prime, eliminate all multiples of p.
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
        p += 1

    primes = []
    # Collect all numbers that are still prime
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes


def M(p, q, N):
    """
    M(p,q,N) is the biggest integer that divisible by only two distinct prime up to N.
    M(p,q,N) = p^a * q^b where p & q two distinct primes such that p < q (to prevent the overcounting)
    """
    max_number = 0
    # Start with p^1
    p_power = 1
    p_prime = p**p_power
    # q must also appear at least once, so we check p_prime * q <= N
    while p_prime * q <= N:
        # start q from q^1
        q_power = 1
        q_prime = q**q_power
        # Try all values p^a * q^b that are <= N
        while p_prime * q_prime <= N:
            value = p_prime * q_prime
            # Take the biggest valid value
            if value > max_number:
                max_number = value
            # Move to the next power of q
            q_power += 1
            q_prime = q**q_power
        # Move to the next power of p
        p_power += 1
        p_prime = p**p_power

    return max_number


def S(N):
    """
    Find the S(N) = ∑M(p,q,N)
    """
    total = 0
    # we need to find all primes up to N
    prime_list = sieve(N)

    # find all the (p,q) pairs from prime_list
    for i in range(len(prime_list) - 1):
        p = prime_list[i]
        # p < q
        for j in range(i + 1, len(prime_list)):
            q = prime_list[j]
            # stop the code when multiplication of the primes larger then N
            if p * q > N:
                break
            # find the all the largest number that is divisible by 2 distinct prime
            M_n = M(p=p, q=q, N=N)
            # add all the M_n in total
            total += M_n
    return total


if __name__ == "__main__":
    begin = time.time()
    result = S(limit)
    end = time.time()
    print(f"Result of problem 347 is {result}.")
    print(f"Finished in {end - begin} seconds.")
