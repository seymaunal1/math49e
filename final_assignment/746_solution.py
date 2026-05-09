#problem 746: level 16

import time


# from the our algorithm the
# S(n) =∑∑(-1)**j * C(k,j) * 2 * j! * (4k/4k-3j) * (C(4k - 3j, j)) * 4 **j * ((2k-2j)!)**2
# Also we take the modulo for every calculation to obtained relatively small numbers each time.
def solve_problem_746(N:int, MOD:int, MAXF: int):
    # factorial list, since we will recall the factorials many times we can not use factorial() method from math
    # we need efficient way to write it
    fact = [1] * (MAXF + 1)
    inverse_fact = [1] * (MAXF + 1)
    for i in range(1, MAXF + 1):
        fact[i] = fact[i - 1] * i % MOD
    # according to fermat's litte theorem MAXF**-1 = MAXF ** MOD-2 (mod MOD)
    inverse_fact[MAXF] = pow(fact[MAXF], MOD - 2, MOD)
    # calculate the inverse factorial to write combinatorial function
    for i in range(MAXF, 0, -1):
        inverse_fact[i - 1] = inverse_fact[i] * i % MOD
    # combinatoric function
    def C(n, r):
        # eliminate edge cases
        if r < 0 or r > n:
            return 0
        # n! / (n-r)!r!
        return fact[n] * inverse_fact[r] % MOD * inverse_fact[n - r] % MOD
    def M(k):
        """
        M(k) = ∑(-1)**j * C(k,j) * 2 * j! * (4k/4k-3j) * (C(4k - 3j, j)) * 4 **j * ((2k-2j)!)**2
        """
        ans = 0
        for j in range(k + 1):
            term = 1
            # r = ((2k-2j)!)**2
            r = 2 * k - 2 * j
            blocks = (4 * k) * pow(4 * k - 3 * j, MOD - 2, MOD) * C(4 * k - 3 * j, j)* fact[r]* fact[r]
            term = term * C(k, j) * 2 * fact[j] * blocks * pow(4, j)
            # inclusion-exlusion principle
            ans += term * (-1)**j
        return ans
    return sum(M(k) for k in range(2, N + 1)) % MOD

MOD = 10**9 + 7 # given modulo= 1.000.000.007
N = 2021 # given n= 2021
MAXF = 4 * N  # number of people in N many family

if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_746(N=N, MOD=MOD, MAXF=MAXF)
    end = time.perf_counter()

    print(f"Result of problem 746 is {result}.")
    print(f"Finished in {end - begin} seconds.")

