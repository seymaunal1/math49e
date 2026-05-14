# problem 137: Fibonacci Golden Nuggets

# In this problem even though the code is simple, algortihm is the essential part of the assignment.

# After writing generating function of the Fibonacci sequence, we get quadratic function that show the
# relationship between Lucas and Fibonacci numbers:
# y - 5k**2 = -4

import time


# From previous assignments, I used the fibonacci function to find last element of fibonacci
# to calculate lucas numbers.
def fibonacci(j: int):
    F = [0, 1]
    for _ in range(2, j + 1):
        F.append(F[-1] + F[-2])
    # Just take the last element of the fibonacci
    return F[-1]


def lucas_numbers(k):
    """
    The formula of the lucas numbers is L_n = F_n+1 + F_n-1 and from the algorithm I found j = 4 * k + 1
    """
    j = 4 * k + 1

    F_j1 = fibonacci(j + 1)
    F_j_1 = fibonacci(j - 1)

    # L_n = F_n+1 + F_n-1
    L_j = F_j1 + F_j_1
    return L_j


def golden_nugget(k):
    # In the algorithm we deduce that L_j = 5 * n + 1
    n = (lucas_numbers(k) - 1) // 5
    return n


if __name__ == "__main__":
    begin = time.time()
    result = golden_nugget(k=15)
    end = time.time()
    print(f"Result of problem 137 is {result}.")
    print(f"Finished in {end - begin} seconds.")
