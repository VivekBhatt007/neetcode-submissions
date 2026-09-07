# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inorderHelper(root, res) -> List[int]:
    if not root:
        return
    inorderHelper(root.left, res)
    res.append(root.val)
    inorderHelper(root.right, res)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        inorderHelper(root, res)
        return res
        