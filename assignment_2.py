import timeit

from math49emodule import IntegerTreeNode, get_files_path


def solve_problem_67_example() -> None:
    # example = "3\n7 4\n2 4 6\n8 5 9 3\n"

    level3 = [
        IntegerTreeNode(8),
        IntegerTreeNode(5),
        IntegerTreeNode(9),
        IntegerTreeNode(3),
    ]

    level2 = [
        IntegerTreeNode(2, level3[0], level3[1]),
        IntegerTreeNode(4, level3[1], level3[2]),
        IntegerTreeNode(6, level3[2], level3[3]),
    ]

    level1 = [
        IntegerTreeNode(7, level2[0], level2[1]),
        IntegerTreeNode(4, level2[1], level2[2]),
    ]

    root = IntegerTreeNode(3, level1[0], level1[1])
    root.walk_tree()


def solve_problem_67() -> None:
    with open(get_files_path() / "0067_triangle.txt") as file:
        print(file.read())


if __name__ == "__main__":
    begin = timeit.timeit()
    solve_problem_67_example()
    # solve_problem_67()
    end = timeit.timeit()
    print(f"Finished in {end - begin} seconds.")
