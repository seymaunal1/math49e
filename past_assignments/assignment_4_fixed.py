import time


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def solve_problem_543(n: int) -> int:
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    total = 2

    # Replaced 101 with n + 1
    for i in range(4, n + 1):
        if i > 3 and i % 2 == 0:
            par_number = i // 2 - 1
        else:
            if is_prime(i):
                if is_prime(i - 2):
                    par_number = i // 2
                else:
                    par_number = i // 2 - 1
            else:
                if is_prime(i - 2):
                    par_number = i // 2 - 1
                else:
                    par_number = i // 2 - 2
        total += par_number

    return total


if __name__ == "__main__":
    begin = time.perf_counter()

    # Generate Fibonacci sequence based on standard definition F(0)=0, F(1)=1
    fib = [0, 1]
    for _ in range(2, 45):
        fib.append(fib[-1] + fib[-2])

    # Sum the results for S(F(k)) over 3 <= k <= 44
    final_result = 0
    for k in range(3, 45):
        final_result += solve_problem_543(fib[k])

    end = time.perf_counter()

    print(f"Result of problem 543 is {final_result}.")
    print(f"Finished in {end - begin} seconds.")
