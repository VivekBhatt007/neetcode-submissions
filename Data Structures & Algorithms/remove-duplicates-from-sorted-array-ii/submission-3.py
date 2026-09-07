class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)
        
        l = 0
        for num in nums:
            if l < 2 or num != nums[l - 2]:
                nums[l] = num
                l += 1
        return l
        # l = 1
        # found_dup = 0
        # for r in range(1, len(nums)):
        #     # if found_dup == 0 and nums[r] == nums[r-1]:
        #     #     nums[l] = nums[r]
        #     #     l += 1
        #     #     found_dup = 1
        #     # if nums[r] != nums[r-1]:
        #     #     nums[l] = nums[r]
        #     #     l += 1
        #     #     found_dup = 0
        #     if nums[r] != nums[r-1]:
        #         nums[l] = nums[r]
        #         l += 1
        #         found_dup = 0
        #     elif found_dup == 0:
        #         nums[l] = nums[r]
        #         l += 1
        #         found_dup = 1
        # return l
        