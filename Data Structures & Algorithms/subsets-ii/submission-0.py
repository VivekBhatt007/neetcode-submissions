class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        curr = []
        def dfsHelper(i):
            if i >= len(nums):
                return res.append(curr[:])

            curr.append(nums[i])
            dfsHelper(i + 1)
            curr.pop()

            while i+1 <len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfsHelper(i + 1)

        dfsHelper(0)
        return res       