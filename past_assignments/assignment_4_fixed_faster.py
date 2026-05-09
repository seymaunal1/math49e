import time


def solve_problem_543() -> int:
    # Generate Fibonacci sequence up to F(44)
    fib = [0, 1]
    for _ in range(2, 45):
        fib.append(fib[-1] + fib[-2])

    max_n = fib[44]  # 701408733

    # Build Sieve of Eratosthenes (Instant Prime Lookup)
    print("Building Sieve of Eratosthenes (This might take ~10-20 seconds) ...")
    is_prime = bytearray([1]) * (max_n + 1)
    is_prime[0] = is_prime[1] = 0
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            # Mark all multiples as not prime
            is_prime[i * i : max_n + 1 : i] = bytearray([0]) * len(
                range(i * i, max_n + 1, i)
            )
    print("Sieve built! Starting the main loop ...")

    # Single-pass calculation
    total = 0
    final_result = 0
    fib_idx = 3  # We start tracking at F(3)

    for i in range(2, max_n + 1):
        # Base cases from your original code
        if i == 2:
            total = 1
        elif i == 3:
            total = 2
        else:
            # Your exact logic, just using array lookups instead of function calls
            if i % 2 == 0:
                par_number = i // 2 - 1
            else:
                if is_prime[i]:
                    if is_prime[i - 2]:
                        par_number = i // 2
                    else:
                        par_number = i // 2 - 1
                else:
                    if is_prime[i - 2]:
                        par_number = i // 2 - 1
                    else:
                        par_number = i // 2 - 2

            total += par_number

        # If our current number 'i' is the next Fibonacci number, save the total
        if i == fib[fib_idx]:
            final_result += total
            fib_idx += 1
            if fib_idx > 44:
                break

    return final_result


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_543()
    end = time.perf_counter()

    print(f"Result of problem 543 is {result}.")
    print(f"Finished in {end - begin} seconds.")
