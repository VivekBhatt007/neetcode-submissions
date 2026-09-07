class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = []
        for idx, n in enumerate(nums):
            tmp = target - n
            if tmp in mp:
                res.append(mp[tmp])
                res.append(idx)
                return res
            else:
                mp[n] = idx
        

        