from __future__ import annotations

from pathlib import Path
from typing import Generic, Optional, TypeVar


def get_files_path() -> Path:
    return Path(__file__).parent / "files"


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
    def walk_tree(self, node: Optional[TreeNode[int]] = None, sum: int = 0) -> None:
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

            self.walk_tree(
                node.left_child
                if node.left_child.data > node.right_child.data
                else node.right_child,
                sum,
            )
        else:
            print("=", sum)

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
