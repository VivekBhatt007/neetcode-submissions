class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        res = 0
        curr = 0
        for n in nums:
            nNum = n - 1
            if nNum not in nset:
                curr = 1
                nextNum = n + 1
                while nextNum in nset:
                    curr += 1
                    nextNum += 1
                res = max(res, curr)
        return res

        