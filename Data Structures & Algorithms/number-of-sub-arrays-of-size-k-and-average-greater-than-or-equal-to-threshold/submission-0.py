class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        w_sum = 0
        for r in range(len(arr)+1):
            if r - l >= k:
                avg = w_sum / k
                if avg >= threshold:
                    res += 1
                w_sum -= arr[l]
                l += 1
            if r < len(arr):
                w_sum += arr[r]
        return res
        