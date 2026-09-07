class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        sub = []
        def dfsHelper(i):
            if i >= len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            dfsHelper(i + 1)

            sub.pop()
            dfsHelper(i + 1)
        
        dfsHelper(0)
        return res
        