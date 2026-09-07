class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s , f = 0 , 0
        while True:
            if s < 0 or s >= len(nums):
                return -1
            s = nums[s]
            if f < 0 or f >= len(nums) or nums[f] < 0 or nums[f] >= len(nums):
                return -1
            f = nums[nums[f]]
            if s == f:
                break
        s1 = 0
        while True:
            s1 = nums[s1]
            s = nums[s]
            if s == s1:
                return s
        return -1

        
        