class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # maxSum = nums[0]
        # minSum = nums[0]

        # currMax = 0
        # currMin = 0
        # total = 0
        # for n in nums:
        #     currMax = max(n, currMax + n)
        #     maxSum = max(maxSum, currMax)

        #     currMin = min(n, currMin + n)
        #     minSum = min(minSum, currMin)
        #     total += n
        
        # if maxSum < 0:
        #     return maxSum
        # return max(maxSum, total - minSum)
        
        l = len(nums)

        pre = [0] * (2*l + 1)
        for i in range(2*l):
            pre[i+1] = pre[i] + nums[i%l]
        
        res = nums[0]
        q = deque([0])
        for i in range(1, 2*l +1):
            if q and q[0] < i - l:
                q.popleft()
            res = max(res, pre[i] - pre[q[0]])

            while q and pre[i] <= pre[q[-1]]:
                q.pop()
            q.append(i)
        return res
