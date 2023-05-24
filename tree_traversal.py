# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        return self.in_order_traversal_impl(root, answer)

    def traversal_impl(self, root: Optional[TreeNode], answer: Optional[List[int]]) -> List[int]:
        if root is None:
            return answer

        while (root.val is not None):
            self.traversal_impl(root.left, answer)
            answer.append(root.val)
            self.traversal_impl(root.right, answer)
            return answer

    def in_order_traversal_impl(self, root: Optional[TreeNode], answer: Optional[List[int]]) -> List[int]:
        answer = []
        if root is None:
            return answer
        visited = set()
        to_visit = [root]
        while len(to_visit) > 0:
            current = to_visit(0)

            if current.left is not None and current.left not in visited:
                to_visit.insert(current.left, 0)
            elif current is not None and current not in visited:
                visited.add(current)
                answer.append(current.val)
            elif current.right is not None and current.right not in visited:
                to_visit.insert(current.right, 0)
        return answer

def main():


#Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
