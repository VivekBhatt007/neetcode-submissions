class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        res = 1
        prev_s = 0
        for r in range(1, len(arr)):
            if arr[r-1] > arr[r]:
                curr_s = 1
            elif arr[r-1] < arr[r]:
                curr_s = -1
            else:
                curr_s = 0

            if curr_s == 0:
                l = r
            elif curr_s == prev_s:
                l = r - 1
            
            prev_s = curr_s
            res = max(res, r - l + 1)
        return res

        