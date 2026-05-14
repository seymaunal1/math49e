import time
from decimal import Decimal, getcontext


def solve_problem_469() -> str:
    # Set precision high enough to ensure 14 decimal places are accurate
    getcontext().prec = 50

    # E_limit = (1 + exp(-2)) / 2
    # For N = 10^18, the convergence is absolute for 14 decimal places.
    e_inv_2 = Decimal(-2).exp()
    result = (Decimal(1) + e_inv_2) / Decimal(2)

    # Format to 14 decimal places
    return format(result, ".14f")


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_469()
    end = time.perf_counter()

    print(f"Result of problem 469 is {result}.")
    print(f"Finished in {end - begin} seconds.")

    assert result == "0.56766764161831", "The result is wrong"
