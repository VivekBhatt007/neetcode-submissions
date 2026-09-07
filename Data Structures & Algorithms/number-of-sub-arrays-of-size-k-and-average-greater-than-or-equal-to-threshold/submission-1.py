class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        w_sum = 0
        t_sum = threshold * k
        # for r in range(len(arr)+1):
        #     if r - l >= k:
        #         avg = w_sum / k
        #         if avg >= threshold:
        #             res += 1
        #         w_sum -= arr[l]
        #         l += 1
        #     if r < len(arr):
        #         w_sum += arr[r]
        # return res
        for r in range(len(arr)):
            w_sum += arr[r]
            if r - l +1 >= k:
                if w_sum >= t_sum:
                    res += 1
                w_sum -= arr[l]
                l += 1
        return res
        