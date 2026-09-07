class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        count = 0
        for idx in range(len(nums)):
            if nums[idx] == 1:
                count = count +1
                max_ones = max(count, max_ones)
            else:
                count = 0
        return max_ones

        