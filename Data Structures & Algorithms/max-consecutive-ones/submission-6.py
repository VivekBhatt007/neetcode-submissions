class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # max_ones = 0
        # count = 0
        # for idx in range(len(nums)):
        #     if nums[idx] == 1:
        #         count = count +1
        #         max_ones = max(count, max_ones)
        #     else:
        #         count = 0
        # return max_ones
        max_ones = 0
        count = 0
        for num in nums:
            if num == 0:
                max_ones = max(count, max_ones)
                count = 0
            else:
                count = count + 1
        return max(max_ones, count)

        