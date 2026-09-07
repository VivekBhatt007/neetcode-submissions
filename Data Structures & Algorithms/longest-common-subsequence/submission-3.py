class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        # dp = [[0]*l2 for _ in range(l1)]
        # def dfs(n1, n2, cache) -> int:
        #     if n1 == l1 or n2 == l2:
        #         return 0
            
        #     if (n1,n2) in cache:
        #         return cache[(n1,n2)]
        #     count = 0
        #     if text1[n1] == text2[n2]:
        #         count = 1 + dfs(n1+1, n2+1, cache)
        #     else:
        #         count += max(dfs(n1+1, n2, cache), dfs(n1, n2+1, cache))
        #     cache[(n1,n2)] = count
        #     return count
        
        # return dfs(0, 0, {})
        dp = [[0]*(l1+1) for _ in range(l2+1)]
        for i in range(l2-1, -1, -1):
            for j in range(l1-1, -1, -1):
                if text1[j] == text2[i]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]

        # cache = {}
        # for i in range(l2):
        #     for j in range(l1):
        #         if text1[j] == text2[i]:
        #             cache[(i,j)] = 1 + cache.get((i+1,j+1), 0)
        #         else:
        #             cache[(i, j)] = max(cache.get((i-1, j), 0), cache.get((i, j-1), 0))
        # return cache[(l2-1, l1-1)]
        


        