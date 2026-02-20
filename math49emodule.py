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

    def set_data(self, data: Type) -> None:
        self.data = data

    def set_left_child(self, left_child: TreeNode[Type]) -> None:
        self.left_child = left_child

    def set_right_child(self, right_child: TreeNode[Type]) -> None:
        self.right_child = right_child

    def get_data(self) -> Optional[Type]:
        return self.data

    def get_left_child(self) -> Optional[TreeNode[Type]]:
        return self.left_child

    def get_right_child(self) -> Optional[TreeNode[Type]]:
        return self.right_child
