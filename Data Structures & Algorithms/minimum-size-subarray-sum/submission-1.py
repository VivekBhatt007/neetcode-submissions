class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float("inf")
        l = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                min_len = min(r - l + 1, min_len)
                s -= nums[l]
                l += 1
        return 0 if min_len == float("inf") else min_len
        