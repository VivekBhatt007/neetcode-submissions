class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for n in nums:
            if n not in mp:
                mp[n] = 1
            else:
                return True
        return False
        