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


def solve_example_problem() -> None:
    example = "3\n7 4\n2 4 6\n8 5 9 3\n"
    root = parse_triangle(example)
    root.walk_tree()


def solve_problem_18() -> None:
    with open(get_files_path() / "0018_triangle.txt") as file:
        root = parse_triangle(file.read())
        root.walk_tree()


def solve_problem_67() -> None:
    with open(get_files_path() / "0067_triangle.txt") as file:
        root = parse_triangle(file.read())
        root.walk_tree()


if __name__ == "__main__":
    functions = [solve_example_problem, solve_problem_18, solve_problem_67]

    for index, function in enumerate(functions):
        print(f"Result of {function.__name__} is:", end=" ")
        begin = time.perf_counter()
        function()
        end = time.perf_counter()
        print(f"Finished in {end - begin} seconds.")

        if index < len(functions) - 1:
            print()
