class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        target_len = float("inf")
        l = 0
        s = 0
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                target_len = min(r - l + 1, target_len)
                s -= nums[l]
                l += 1
        return 0 if target_len == float("inf") else target_len
        