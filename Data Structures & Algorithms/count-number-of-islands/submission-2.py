class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfsHelper(r, c):
            R = len(grid)
            C = len(grid[0])
            if min(r,c) < 0:
                return
            if r == R or c == C:
                return
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfsHelper(r - 1, c)
            dfsHelper(r + 1, c)
            dfsHelper(r, c + 1)
            dfsHelper(r, c - 1)
            return
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfsHelper(r, c)
        return count



        