class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # s = 1
        # e = len(arr)
        # ns = s
        # cnt = 0
        # while s < e :
        #     if arr[s] > arr[s-1] :
        #         ns = s - 1
        #         arr[s-1] = arr[s]
        #         while ns > 0 and arr[s] > arr[ns]:
        #             arr[ns] = arr[s]
        #             ns -= 1
        #         cnt += 1
        #         if cnt == 10:
        #             break
        #         print(arr)
        #         s += 1
        # return arr
        res = [0] * len(arr)
        max_val = -1
        for idx in range(len(arr) - 1, -1, -1):
            res[idx] = max_val
            if arr[idx] > max_val:
                max_val = arr[idx]
        return res

# 
# [17,18,5,4,6,1]
#      s
#  s-1
#  ns
# 
# 

