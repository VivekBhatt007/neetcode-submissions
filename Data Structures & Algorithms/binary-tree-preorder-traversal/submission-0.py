# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = []
        curr = root

        res = []
        while curr or st:
            if curr:
                res.append(curr.val)
                if curr.right:
                    st.append(curr.right)
                curr = curr.left
            else:
                curr = st.pop()
        return res
        