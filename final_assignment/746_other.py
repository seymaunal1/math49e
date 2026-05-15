# type: ignore

import time

"""
This is a alternative solution for problem 746:
* ving
* https://projecteuler.net/quote_post=376518
"""
"""
- Total time of alternative solution: 5.711833953857422
- Total time of my solution: 6.9735742919147015
- The result: 867150922

The main reason for this difference:
* Their solution used a more optimized version of the formula e.g. they simplified the block placement part
from j! * (4n / (4n - 3j)) * C(4n - 3j, j)
to 4n * (j - 1)! * C(4n - 3j - 1, j - 1) while I directly apply the mathematical formula.
* Also, their code precomputes combinations in a choose table, so it can get them by simple list indexing,
while my code recalculates them through the C() function.
* Another difference is that compare to their code I did not take modulo to obtained relatively small number.
So, the first solution is more efficient because it avoids repeated modular inverse calculations,
uses faster precomputed combination lookups, and keeps the intermediate values smaller during the calculation.
"""

begin = time.time()

N = 2  # M(N) = 896
N = 3  # M(N) = 890880
N = 10  # S(N) % MOD = 399291975
N = 2021  # S(N) = 867150922

MOD = 1000000007

# factorial list for fast factorial calculation
fact = (4 * N + 1) * [1]
choose = [[1], [1, 1]]

# precompute factorials and combination values up to 4*N
for n in range(2, 4 * N + 1):
    fact[n] = n * fact[n - 1] % MOD
    row = choose[-1]
    choose.append([1] + [(row[k - 1] + row[k]) % MOD for k in range(1, n)] + [1])


# calculate one term of M(n)
def f(n, k):
    if k == 0:
        return 2 * fact[2 * n] ** 2 % MOD
    else:
        # variables after simplifying the formula
        k_1 = k - 1
        n_k = n - k
        # optimized formula for the k-th term
        return (
            choose[n][k]
            * fact[k_1]
            * 8
            * n
            * pow(4, k, MOD)
            * choose[4 * n_k + k_1][k_1]
            * fact[2 * n_k] ** 2
            % MOD
        )


# M(n) is calculated from part f(n,k) and in this part it's alternating
def M(n):
    sign = 1
    s = 0
    # inclusion-exclusion principle
    for k in range(n + 1):
        s += sign * f(n, k)
        sign = -sign
    return s


# take the summation of M(n)
S = sum(M(n) for n in range(2, N + 1))

end = time.time()

print(f"Result of problem 746 is {S % MOD}.")
print(f"Finished in {end - begin} seconds.")
