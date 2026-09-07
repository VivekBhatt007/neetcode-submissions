class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        size = len(nums)
        res = [1] * size

        for i in range(1, size):
            res[i] = res[i-1] * nums[i-1]
        
        post = 1
        for i in range(size-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
        # V1
        # preMul = []
        # size = len(nums)
        # postMul = [1] * size
        # left = 1
        # for idx in range(size):
        #     preMul.append(left)
        #     left = left*nums[idx]
        # right = 1
        # for idx in range(size-1, -1, -1):
        #     postMul[idx] =  right
        #     right= right*nums[idx]

        # res = []
        # for idx in range(size):
        #     res.append(preMul[idx]*postMul[idx])
        # return res

        