class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # start = 0
        # end = len(nums) - 1
        # while start <= end:
        #     if nums[start] == val:
        #         if nums[end] == val:
        #             end = end - 1
        #             continue
        #         nums[start], nums[end] = nums[end], nums[start]
        #         start = start + 1
        #         end = end - 1
        #     else:
        #         start = start+1
        # return end +1
        s = 0
        e = len(nums)
        while s < e:
            if nums[s] == val:
                e -= 1
                nums[s] = nums[e]
            else :
                s += 1
        return e
