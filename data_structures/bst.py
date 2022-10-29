from __future__ import annotations
from typing import Iterable, Union


class BST:
    """
    Estrutura de árvore de busca binária
    """

    class Node:
        def __init__(self, value: int, parent=None, left=None, right=None):
            self.value: int = value
            self.left: Union[Node, None] = left
            self.right: Union[Node, None] = right

        def insert(self, value):
            if value < self.value:
                if self.left is None:
                    self.left = BST.Node(value)
                else:
                    self.left.insert(value)
            else:
                if self.right is None:
                    self.right = BST.Node(value)
                else:
                    self.right.insert(value)

        def search(self, value):
            def inner_search(root):
                if root is None or root == value:
                    return root
                if root.value < value:
                    inner_search(root.left)
                else:
                    inner_search(root.right)

            return inner_search(self)

        def __str__(self):
            return str(self.value)

    root: self.Node

    def __init__(self, root, others: Iterable = None):
        self.root = self.Node(root)

        for v in others:
            self.insert(v)

    def insert(self, value):
        self.root.insert(value)

    def search(self, value):
        self.root.search(value)

    def min_from(self, node):
        r = node
        while r.left is not None:
            r = r.left
        return r

    def max_from(self, node):
        r = node
        while r.right is not None:
            r = r.right
        return r

    @property
    def min(self):
        return self.min_from(self.root)

    @property
    def max(self):
        return self.max_from(self.root)

    def __contains__(self, item):
        return root.search(item) is not None

    def __str__(self):
        def show(root_node: Node):
            if root_node is not None:
                l, r = root_node.left, root_node.right
                return f"{root_node.value} ({show(l) if l is not None else '_'} {show(r) if r is not None else '_'})"

        return show(self.root)


if __name__ == "__main__":
    tree = BST(4, [1, 6, 7, 3, 2, 9])
    print(tree)

    print(tree.max)
    print(tree.min)
