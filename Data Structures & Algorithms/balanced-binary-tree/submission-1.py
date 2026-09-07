# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# V1
# def helper(root):
#     if not root:
#         return (True, 0)
    
#     l_h = helper(root.left)
#     r_h = helper(root.right)
#     isBal = abs(l_h[1] - r_h[1]) <= 1
#     h = 1 + max(l_h[1], r_h[1])
#     return (isBal, h)

def height(root) -> int:
    if not root:
        return 0
    
    return 1 + max(height(root.left), height(root.right))

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # res = helper(root)
        # isBal, h = res
        # return isBal
        if not root:
            return True
        l = height(root.left)
        r = height(root.right)
        if abs(l - r) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)









        