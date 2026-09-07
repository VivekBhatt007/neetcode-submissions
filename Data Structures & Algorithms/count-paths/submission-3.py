class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # V1
        # def dfs(r, c, cache) -> int:
        #     if r >= m or c >= n:
        #         return 0
            
        #     if cache[r][c] > 0:
        #         return cache[r][c]
        #     if r == m - 1 and c == n - 1:
        #         return 1

        #     res = dfs(r+1,c, cache) + dfs(r, c+1, cache)
        #     cache[r][c] = res
        #     return res

        # return dfs(0,0, [[0]*n for i in range(m)]) 
        # V2
        # cache = [[0]*m for i in range(n)]
        # cache[n-1][m-1] = 1

        # for r in range(n-1, -1, -1):
        #     for c in range(m-1, -1, -1):
        #         if cache[r][c] != 0:
        #             continue
        #         r_1 = 0
        #         if r+1 == n:
        #             r_1 = 0
        #         else:
        #             r_1 = cache[r+1][c]
        #         c_1 = 0
        #         if c+1 == m:
        #             c_1 = 0
        #         else:
        #             c_1 = cache[r][c+1]
        #         cache[r][c] = r_1 + c_1
        
        # return cache[0][0]
        # V3
        prev_row = [0] * n

        res = 0
        for r in range(m-1, -1 , -1):
            curr_row = [0] * n
            curr_row[n-1] = 1
            for c in range(n-2, -1, -1):
                curr_row[c] = curr_row[c+1] + prev_row[c]
            prev_row = curr_row
            res = curr_row[0]
        return res
                


