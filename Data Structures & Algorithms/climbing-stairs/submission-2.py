class Solution:
    def climbStairs(self, n: int) -> int:

        # def recStair(i):
        #     if i >= n:
        #         return i == n
        #     return recStair(i+1) + recStair(i+2)
        # return recStair(0)
        cache = [-1] * n

        def rec(i):
            if i >= n:
                return i == n
            if cache[i] != -1:
                return cache[i]
            cache[i] = rec(i+1) + rec(i+2)
            return cache[i]

        return rec(0)
        