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


class IntegerTreeNode(TreeNode[int]):
    sum = 0

    def walk_tree(self, node: Optional[TreeNode[int]] = None) -> None:
        if node is None:
            node = self

        if node.data:
            self.sum += node.data

        if (
            node.left_child
            and node.left_child.data
            and node.right_child
            and node.right_child.data
        ):
            self.walk_tree(
                node.left_child
                if node.left_child.data > node.right_child.data
                else node.right_child
            )
        else:
            print(self.sum)
