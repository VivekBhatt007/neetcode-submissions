class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            total += n
        l_sum = 0
        r_sum = 0
        for idx in range(len(nums)):
            r_sum = total - nums[idx] - l_sum
            if l_sum == r_sum:
                return idx
            l_sum += nums[idx]
        return -1

            
        