import time

from math49emodule import IntegerTreeNode, get_files_path


def parse_triangle(input: str) -> IntegerTreeNode:
    rows = [list(map(int, line.split())) for line in input.splitlines()]
    node_rows = [[IntegerTreeNode(value) for value in row] for row in rows]

    for row in range(len(node_rows) - 1):
        for column in range(len(node_rows[row])):
            node_rows[row][column].left_child = node_rows[row + 1][column]
            node_rows[row][column].right_child = node_rows[row + 1][column + 1]

    return node_rows[0][0]


def parse_triangle_simple(input: str) -> list[list[int]]:
    return [list(map(int, line.split())) for line in input.splitlines()]


def get_max_path_sum_bottom_up(triangle: list[list[int]]) -> int:
    for row in range(len(triangle) - 2, -1, -1):
        for column in range(len(triangle[row])):
            left_child = triangle[row + 1][column]
            right_child = triangle[row + 1][column + 1]
            triangle[row][column] += max(left_child, right_child)

    return triangle[0][0]


def solve_example_problem() -> int:
    example: str = "3\n7 4\n2 4 6\n8 5 9 3\n"
    root: IntegerTreeNode = parse_triangle(example)

    return root.walk_tree()


def solve_problem_18() -> int:
    with open(get_files_path() / "0018_triangle.txt") as file:
        root: IntegerTreeNode = parse_triangle(file.read())

    return root.walk_tree_completely()


def solve_problem_18_optimized() -> int:
    with open(get_files_path() / "0018_triangle.txt") as file:
        root: IntegerTreeNode = parse_triangle(file.read())

    return root.walk_tree_optimized()


def solve_problem_67() -> int:
    with open(get_files_path() / "0067_triangle.txt") as file:
        root: IntegerTreeNode = parse_triangle(file.read())

    return root.walk_tree_optimized()


def solve_problem_67_simple() -> int:
    with open(get_files_path() / "0067_triangle.txt") as file:
        triangle: list[list[int]] = parse_triangle_simple(file.read())

    return get_max_path_sum_bottom_up(triangle)


if __name__ == "__main__":
    functions = [
        solve_example_problem,
        solve_problem_18,
        solve_problem_18_optimized,
        solve_problem_67,
        solve_problem_67_simple,
    ]

    for index, function in enumerate(functions):
        begin = time.perf_counter()
        print(f"Result of {function.__name__} is {function()}.")
        end = time.perf_counter()
        print(f"Finished in {end - begin} seconds.")

        if index < len(functions) - 1:
            print()
