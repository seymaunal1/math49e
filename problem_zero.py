import time


# I am so confused about writing return, should I?
# Yes (if you don't pass a value as an argument by reference)
# and make the used variables not global if possible
def get_square_numbers() -> list[int]:
    magic_number = 495000
    square_numbers: list[int] = []

    for i in range(1, magic_number + 1):
        square_numbers.append(i * i)

    return square_numbers


def is_odd(element: int) -> bool:
    return element % 2 != 0


# Find the sum of first 495000 square numbers which are odd
def solve_problem_0() -> int:
    # And you should also save the return value to a variable
    square_numbers: list[int] = get_square_numbers()

    # Filter for odd numbers in the list
    odd_square_numbers = list(filter(is_odd, square_numbers))

    # Can I use reduce function without lambda? Like operator?
    # If you mean with lambda: Yes you can, my smart girlfriend <3
    # sum_of_odd_square_numbers = reduce(lambda x, y: x + y, odd_square_numbers)
    # Butt 😏 the easier way is:
    return sum(odd_square_numbers)


if __name__ == "__main__":
    begin = time.perf_counter()
    result = solve_problem_0()
    end = time.perf_counter()

    print(f"Result of problem zero is {result}.")
    print(f"Finished in {end - begin} seconds.")
