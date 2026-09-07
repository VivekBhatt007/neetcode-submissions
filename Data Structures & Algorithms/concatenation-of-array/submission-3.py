class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
        # n = len(nums)
        # ans = [0] * 2 * n
        # for idx in range(len(ans)):
        #     ans[idx] = nums[idx % n]
        # for idx, num in enumerate(nums):
        #     ans[idx] = ans[idx+n] = num
        return ans