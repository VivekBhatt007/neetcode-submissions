class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(r, c, cache) -> int:
            if r >= m or c >= n:
                return 0
            
            if cache[r][c] > 0:
                return cache[r][c]
            if r == m - 1 and c == n - 1:
                return 1

            res = dfs(r+1,c, cache) + dfs(r, c+1, cache)
            cache[r][c] = res
            return res

        return dfs(0,0, [[0]*n for i in range(m)]) 
        