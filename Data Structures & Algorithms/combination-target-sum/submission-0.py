class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        sub = []
        def dfs(i, s):
            if i >= len(nums) and s != target:
                return
            if s > target:
                return
            if s == target:
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            s += nums[i]
            dfs(i, s)

            sub.pop()
            s -= nums[i]
            dfs(i+1, s)
        
        dfs(0, 0)
        return res
        