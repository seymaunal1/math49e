# problem 340/level:09

import time

MOD = 1_000_000_000


def F(n: int, a: int, b: int, c: int) -> int:
    """
    This is the simplified version of F(a + F(a + F(a + F(a + n)))).
    """
    # it's given that if n bigger than b: F(n) = n - c
    if n > b:
        F_n = n - c
        return F_n % MOD  # to optimize the result.
    # we count the steps that at how many steps we can reach k * n > b
    k = (b - n) // a
    # this function directly result of the algorithm
    F_n = (k + 1) * a - c + n + (k + 1) * 3 * (a - c)
    return F_n


# The result of the problem is independent from F(n),
# however you can uncomment these lines to see F(n) is working:
# print(F(n=0, a=50, b=2000, c=40))
# print(F(n=2000, a=50, b=2000, c=40))


def S(a: int, b: int, c: int) -> int:
    """
    Now we will calculate the sum of F(n) from 0 up to b = 7**21 i.e. S = ∑F(n)
    However it is hard to calculate directly so we will separate the summation.
    And in the algorithm we conclude that the summation of the F_n is independent from F_n formula.
    As it is written in the algorithm we split the S to easier calculation.
    S = sum_k + sum_n - sum_c where
    """
    # b = q*a + r
    q = b // a  # the number of a in b
    r = b % a  # remainder of r

    # sum_n: ∑n = b * (b + 1) // 2
    sum_n = b * (b + 1) // 2
    # sum_c: ∑c:c * (b + 1)
    sum_c = c * (b + 1)
    # sum_k:(4*a - 3*c)*∑(k+1)
    sum_k1 = (q + 1) * (r + 1) + a * q * (q + 1) // 2
    sum_k = sum_k1 * (4 * a - 3 * c)
    # the result of S(n)
    S = sum_k + sum_n - sum_c
    return S % MOD


if __name__ == "__main__":
    begin = time.time()
    result = S(a=21**7, b=7**21, c=12**7)
    end = time.time()

    print(f"Result of problem 340 is {result}.")
    print(f"Finished in {end - begin} seconds.")
