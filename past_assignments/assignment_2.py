from __future__ import annotations

import time
from functools import cache
from typing import Generic, Optional, TypeVar

Type = TypeVar("Type")


class TreeNode(Generic[Type]):
    def __init__(
        self,
        data: Optional[Type] = None,
        left_child: Optional[TreeNode[Type]] = None,
        right_child: Optional[TreeNode[Type]] = None,
    ) -> None:
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        return str(self.data)


class IntegerTreeNode(TreeNode[int]):
    def walk_tree(self, node: Optional[TreeNode[int]] = None, sum: int = 0) -> int:
        if node is None:
            node = self

        if node.data:
            print(node.data, end=" ")
            sum += node.data

        if (
            node.left_child
            and node.left_child.data
            and node.right_child
            and node.right_child.data
        ):
            print("+", end=" ")
            return self.walk_tree(
                node.left_child
                if node.left_child.data > node.right_child.data
                else node.right_child,
                sum,
            )
        else:
            print("=", sum)
            return sum

    def walk_tree_completely(
        self, node: Optional[TreeNode[int]] = None, sum: int = 0
    ) -> int:
        if node is None:
            node = self

        if node.data:
            sum += node.data

        # If we are at a leaf node, return this path's sum
        if not node.left_child and not node.right_child:
            return sum

        # Variables to store the highest sums from our left and right branches
        left_max = 0
        right_max = 0

        # Recursively find the maximum values in left and right branches
        if node.left_child:
            left_max = self.walk_tree_completely(node.left_child, sum)

        if node.right_child:
            right_max = self.walk_tree_completely(node.right_child, sum)

        # Return whichever branch gave us the bigger number
        return max(left_max, right_max)

    # TODO: Remove this @cache and see the difference 🤯😘
    @cache
    def walk_tree_optimized(self, node: Optional[TreeNode[int]] = None) -> int:
        if node is None:
            node = self

        # If we are at a leaf node, return its data
        if not node.left_child and not node.right_child:
            return node.data or 0

        # Get the max sum of the left and right branches
        left_max = 0
        right_max = 0

        if node.left_child:
            left_max = self.walk_tree_optimized(node.left_child)

        if node.right_child:
            right_max = self.walk_tree_optimized(node.right_child)

        # Add this node's data to the bigger of the two branches and return it up
        return (node.data or 0) + max(left_max, right_max)


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


def get_max_path_sum(triangle: list[list[int]]) -> int:
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
    with open("0018_triangle.txt") as file:
        root: IntegerTreeNode = parse_triangle(file.read())

    return root.walk_tree_completely()


def solve_problem_18_optimized() -> int:
    with open("0018_triangle.txt") as file:
        root: IntegerTreeNode = parse_triangle(file.read())

    return root.walk_tree_optimized()


def solve_problem_18_simple() -> int:
    with open("0018_triangle.txt") as file:
        triangle: list[list[int]] = parse_triangle_simple(file.read())

    return get_max_path_sum(triangle)


def solve_problem_67_optimized() -> int:
    with open("0067_triangle.txt") as file:
        root: IntegerTreeNode = parse_triangle(file.read())

    return root.walk_tree_optimized()


def solve_problem_67_simple() -> int:
    with open("0067_triangle.txt") as file:
        triangle: list[list[int]] = parse_triangle_simple(file.read())

    return get_max_path_sum(triangle)


if __name__ == "__main__":
    functions = [
        solve_example_problem,
        solve_problem_18,
        solve_problem_18_optimized,
        solve_problem_18_simple,
        solve_problem_67_optimized,
        solve_problem_67_simple,
    ]

    for index, function in enumerate(functions):
        begin = time.perf_counter()
        result = function()
        end = time.perf_counter()

        print(f"Result of {function.__name__} is {result}.")
        print(f"Finished in {end - begin} seconds.")

        if index < len(functions) - 1:
            print()
