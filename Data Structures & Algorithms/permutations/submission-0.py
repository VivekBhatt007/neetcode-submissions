class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        return helper(0, nums)

def helper(idx, nums):
    if idx == len(nums):
        return [[]]
    
    resParam = []
    param = helper(idx+1, nums)
    for p in param:
        for i in range(len(p) + 1):
            pCopy = p.copy()
            pCopy.insert(i, nums[idx])
            resParam.append(pCopy)
    return resParam
