import time
from fractions import Fraction
from math import exp

begin = time.time()

def solve_problem_469():

    def A_n(number):
        A = [Fraction(0) for _ in range(number + 1)]

        if number >= 1:
            A[1] = Fraction(1)

        for n in range(2, number + 1):
            A[n] = Fraction(
                (n - 1) * A[n - 1] + 2 * A[n - 2] + 1,
                n
            )

        return A


    number = 1000
    A = A_n(number)

#    print("n\tA_n\t\tA_n/n\t\td_n")
#    print("-" * 80)

    for n in range(1, number + 1):
        d_n = A[n] - A[n - 1]
    #    print(f"{n}\t{float(A[n]/n)}\t{float(d_n)}")


    E_n = 1 - ((1-exp(-2))/2)
    return E_n

if __name__ == "__main__":
    begin = time.time()
    result = solve_problem_469()
    end = time.time()

    print(f"Result of problem 469 is {result}.")
    print(f"Finished in {end - begin} seconds.")

