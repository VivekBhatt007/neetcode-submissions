class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        res = [0] * (n+1)
        res[0] = 0
        res[1] = 1
        for i in range(1, n+1):
            # if i & (i - 1) == 0:
            #     res[i] = 1
            # else:
            res[i] = res[i//2] + (i % 2)
        return res
        