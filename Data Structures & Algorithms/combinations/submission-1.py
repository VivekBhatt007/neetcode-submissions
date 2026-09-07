class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        helper(1, [], res, n, k)
        return res
    

def helper(i, curr, res, n, k):
    if len(curr) == k:
        res.append(curr.copy())
        return
        
    if i > n:
        return
        
    curr.append(i)
    helper(i+1, curr, res, n, k)

    curr.pop()
    helper(i+1, curr, res, n, k)
        