import time


# This function reads the triangle input and converts it into list of list integers.
def parse_triangle(input: str) -> list[list[int]]:
    return [list(map(int, line.split())) for line in input.splitlines()]


# This function calculates the maximum path sum.
# It starts from bottom to up and moves to the upward.
def get_max_path_sum(triangle: list[list[int]]) -> int:
    # It starts to iterate from the second last row up to to the top row.
    for row in range(len(triangle) - 2, -1, -1):
        # For each iteration, compare its left and right child.
        for column in range(len(triangle[row])):
            left_child = triangle[row + 1][column]
            right_child = triangle[row + 1][column + 1]
            # Add the maximum of the two children to the current element.
            triangle[row][column] += max(left_child, right_child)

    return triangle[0][0]


# This function reads the triangle data from the file,
# parses it, and returns the maximum path sum.
def solve_problem_67() -> int:
    with open("0067_triangle.txt") as file:
        triangle: list[list[int]] = parse_triangle(file.read())

    return get_max_path_sum(triangle)


if __name__ == "__main__":
    begin = time.perf_counter()
    result: int = solve_problem_67()
    end = time.perf_counter()

    print(f"Result of problem 67 is {result}.")
    print(f"Finished in {end - begin} seconds.")
