# problem 469: level 16
import time
from fractions import Fraction
from math import exp

begin = time.time()
"""
* E(N): expected fraction of empty chairs around the round table
* E(N): 1 - {expected number of seated knights around the round table}
* {expected number of seated knights around the round table}: 1 + A(N-3)
* A(N): refers to the number of seated knights in a row of n chairs
* since after first person seat, the round table transformed to the row table.
"""
def solve_problem_469():
    """
    First our aim is find limit of A(n)/n
    """

    # A(n) = 1 + 2/n * ∑A(i) where i = 0,1....n-2
    def A_n(number):
        A = [Fraction(0) for _ in range(number + 1)]
        # We know A(1) = 1
        if number >= 1:
            A[1] = Fraction(1)
        # In the algorithm, we conclude that the generating function of A(n) is:
        #  n* A(n) = (n - 1) * A[n - 1] + 2 * A[n - 2] + 1
        for n in range(2, number + 1):
            A[n] = Fraction((n - 1) * A[n - 1] + 2 * A[n - 2] + 1, n)
        return A

    number = 1000
    # I put every A(n)'s in a list up to 1000 to find their limit.
    A = A_n(number)

    #    print("n\tA_n\t\tA_n/n\t\td_n")
    #    print("-" * 80)
    # In here, I looked at the increment of A(n) and compare to the A(n)/n and we can easily see that
    # after some n, the A(n)/n ~ d_n = 0.43233235838169 and  we know that this number is the result of
    # (1 - e **2) / 2
    for n in range(1, number + 1):
        d_n = A[n] - A[n - 1]

        # You can uncomment this line if you want to see the results of d_n and A[n]/n.
        # print(f"{n}\t{float(A[n]/n)}\t{float(d_n):.14f}")

    # Because of the previous calculations, we will calculate E_n = 1 - ((1 - e **2) / 2)
    E_n = 1 - ((1 - exp(-2)) / 2)

    return f"{E_n:.14f}"


if __name__ == "__main__":
    begin = time.time()
    result = solve_problem_469()
    end = time.time()

    print(f"Result of problem 469 is {result}.")
    print(f"Finished in {end - begin} seconds.")
