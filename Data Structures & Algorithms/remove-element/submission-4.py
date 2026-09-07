class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            if nums[start] == val:
                if nums[end] == val:
                    end = end - 1
                    continue
                nums[start], nums[end] = nums[end], nums[start]
                start = start + 1
                end = end - 1
            else:
                start = start+1
        return end +1
