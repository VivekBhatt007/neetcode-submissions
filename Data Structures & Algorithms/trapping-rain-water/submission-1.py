class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        l = 0
        r = n - 1
        lMax = height[0]
        rMax = height[r]
        res = 0
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax -  height[r]
        return res

        # lMax = [height[0]]
        # rMax = [0] * n
        # rMax[n-1] = height[n-1]
        # for idx in range(1, n):
        #     lMax.append(max(lMax[idx-1], height[idx]))
        #     rMax[n-idx-1] = max(rMax[n-idx], height[n-idx-1])
        # res = 0
        # for i in range(n):
        #     res += min(lMax[i], rMax[i]) - height[i]
        
        # return res
            
        