class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res
        currSum = 0
        res = 0
        preSum = { 0 : 1}
        for n in nums:
            currSum += n
            diff = currSum - k
            res += preSum.get(diff, 0)
            preSum[currSum] = 1 + preSum.get(currSum, 0)
        return res
        