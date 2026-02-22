import timeit

from math49emodule import IntegerTreeNode, get_files_path


def parse_triangle(input: str) -> IntegerTreeNode:
    rows = [list(map(int, line.split())) for line in input.splitlines()]
    node_rows = [[IntegerTreeNode(value) for value in row] for row in rows]
    print(node_rows)

    for r in range(len(node_rows) - 1):
        for c in range(len(node_rows[r])):
            node_rows[r][c].left_child = node_rows[r + 1][c]
            node_rows[r][c].right_child = node_rows[r + 1][c + 1]

    return node_rows[0][0]


def solve_problem_67_example() -> None:
    example = "3\n7 4\n2 4 6\n8 5 9 3\n"
    root = parse_triangle(example)
    root.walk_tree()


def solve_problem_67() -> None:
    with open(get_files_path() / "0067_triangle.txt") as file:
        root = parse_triangle(file.read())
        root.walk_tree()


# check the time again
if __name__ == "__main__":
    begin = timeit.timeit()
    solve_problem_67_example()
    solve_problem_67()
    end = timeit.timeit()
    print(f"Finished in {end - begin} seconds.")
