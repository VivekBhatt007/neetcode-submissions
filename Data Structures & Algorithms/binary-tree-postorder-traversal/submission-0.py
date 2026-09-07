# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st = [root]
        visited = [False]
        res = []
        while st:
            curr = st.pop()
            visit = visited.pop()
            if curr:
                if visit:
                    res.append(curr.val)
                else:
                    st.append(curr)
                    visited.append(True)
                    st.append(curr.right)
                    visited.append(False)
                    st.append(curr.left)
                    visited.append(False)
        return res

        