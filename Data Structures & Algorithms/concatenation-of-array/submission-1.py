class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * 2 * n
        for idx in range(len(ans)):
            ans[idx] = nums[idx % n]
        return ans