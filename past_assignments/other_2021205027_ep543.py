# type: ignore

import time

from sympy import primepi as pi

"""
This is an alternative solution for problem 543:
* Mikhail Lomonosov
* https://projecteuler.net/quote_post=438895
"""
"""
- The answer of the problem: 199007746081234640
- Total time of alternative solution: 0.22940802574157715 seconds.
- Total time of my solution: 1.7660038471221924

Main reason for this difference:
The alternative solution uses SymPy's ready-made prime counting function (primepi),
which is already highly optimized. So it runs faster.

However, in my solution I calculated the prime count manually in Python. In my code, I used
loops, dictionary operations, and repeated function calls, which makes it a bit slower.

Or alternative answer:

The difference mainly comes from implementation. The alternative solution relies on an optimized library function,
while my solution does everything step by step in Python. Because of that, my code has more overhead and runs slightly slower.

"""
begin = time.time()
# ready-made function that counts number of prime up to n.
# SymPy must be installed before running this code:
#       pip install sympy


def S(n):
    # number of primes <= n
    r = pi(n)
    # For very small n, the formula simplifies, so we can directly return pi(n)
    if n <= 3:
        return r
    # To find 2-partitions:
    # they found (n - 2 primes) + (number of even numbers) - (exceptions)
    r += pi(n - 2) + n // 2 - 2
    # Similarly, for small n, higher-order terms are not needed,
    if n <= 5:
        return r
    # This term counts a large group of valid pairings by combining numbers up to n/2
    # with numbers up to n.
    r += (n // 2 - 2) * (n + 1)
    # Final correction term:
    return r - (n // 2) * (n // 2 + 1) + 6


# general way to find fibonacci sequence
F = [0, 1]
for k in range(43):
    F.append(F[-1] + F[-2])
end = time.time()

# cFind the sum of all S(F(k)) over 3 <= k <= 44
print(f"Result of problem 543 is {sum(map(S, F[3:]))}.")
print(f"Finished in {end - begin} seconds.")
