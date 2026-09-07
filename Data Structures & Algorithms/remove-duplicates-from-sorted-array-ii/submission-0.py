class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 1
        found_dup = 0
        for r in range(1, len(nums)):
            if found_dup == 0 and nums[r] == nums[r-1]:
                nums[l] = nums[r]
                l += 1
                found_dup = 1
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
                found_dup = 0
        return l
        