# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfsHelper(root, val, targetSum):
            if not root :
                return False
            
            newVal = root.val + val

            if not root.left and not root.right:
                return newVal == targetSum

            # if dfsHelper(root.left, newVal, targetSum):
            #     return True
            # if dfsHelper(root.right, newVal, targetSum):
            #     return True
            
            # return False
            return dfsHelper(root.left, newVal, targetSum) or \
                    dfsHelper(root.right, newVal, targetSum)
        
        return dfsHelper(root, 0, targetSum)
        