class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[-1]

        n = [0] * len(nums)
        n[0] = nums[0]
        n[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            print(f"n-1: {n[i-1]} n-2: {n[i-2]}")
            n[i] = max(nums[i]+n[i-2], n[i-1])
            print(n)
        
        print(f"final: {n}")
        return n[-1]
        