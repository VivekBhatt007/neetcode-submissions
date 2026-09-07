class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i = 0
        # j = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums1[i] >= nums2[j]:
        #         k = len(nums1) -1
        #         while k > i:
        #             nums1[k] = nums1[k-1]
        #             k -= 1
        #         nums1[i] = nums2[j]
        #         i += 1
        #         j += 1
        #     elif nums1[i] == 0:
        #         nums1[i] = nums2[j]
        #         i += 1
        #         j += 1
        #     else:
        #         i += 1

        t_idx = m + n - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[t_idx] = nums1[m - 1]
                m -= 1
            else:
                nums1[t_idx] = nums2[n - 1]
                n -= 1
            t_idx -= 1
        while n > 0:
            nums1[t_idx] = nums2[n - 1]
            n -= 1
            t_idx -= 1


        