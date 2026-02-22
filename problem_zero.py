# find the sum of first 495000 square numbers which are odd
import timeit
from functools import reduce

magic_number = 495000
square_number_list = []


def is_odd(element: int):
    return element % 2 != 0


# I am so confused about writing return, should I?
def square_numbers():
    for i in range(1, magic_number + 1):
        square_number_list.append(i * i)


if __name__ == "__main__":
    begin = timeit.timeit()
    square_numbers()

    # filter for odd numbers in the list
    odd_square = list(filter(is_odd, square_number_list))

    # can I use reduce function without lambda? like operator?
    sum_of_odd_square = reduce(lambda x, y: x + y, odd_square)
    print(sum_of_odd_square)
    end = timeit.timeit()
    print(f"Finished in {end - begin} seconds.")
