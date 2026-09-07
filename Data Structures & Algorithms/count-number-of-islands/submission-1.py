class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfsHelper(grid, r, c):
            R = len(grid)
            C = len(grid[0])
            if min(r,c) < 0:
                return
            if r == R or c == C:
                return
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfsHelper(grid, r - 1, c)
            dfsHelper(grid, r + 1, c)
            dfsHelper(grid, r, c + 1)
            dfsHelper(grid, r, c - 1)
            return
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    dfsHelper(grid, r, c)
        return count



        