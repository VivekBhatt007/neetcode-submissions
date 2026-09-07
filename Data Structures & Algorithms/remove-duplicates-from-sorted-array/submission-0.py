class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for i in range(len(nums) -1):
        #     if nums[i] == nums[i+1]:
        #         j = i+1
        #         while j < len(nums) and nums[j] == nums[i]:
        #             j += 1
        #             dup += 1
        #         k = i + 1
        #         while j < len(nums):
        #             nums[k] = nums[j]
        #             k += 1
        #             j += 1
        # res = 0
        # while nums[res] != nums[res+1]:
        #     res += 1
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l
        