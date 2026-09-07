class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # V1
        # def findArea(r, c, area):
        #     R = len(grid)
        #     C = len(grid[0])
        #     if min(r, c) < 0:
        #         return
        #     if r >= R or c >= C:
        #         return
        #     if grid[r][c] == 0:
        #         return
            
        #     area[0] += 1
        #     grid[r][c] = 0
        #     findArea(r + 1, c, area)
        #     findArea(r - 1, c, area)
        #     findArea(r, c + 1, area)
        #     findArea(r, c - 1, area)
        
        # maxArea = 0
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1:
        #             area = [0]
        #             findArea(r, c, area)
        #             maxArea = max(maxArea, area[0])
        
        # return maxArea
        # V2
        def findArea(r, c) -> int:
            R = len(grid)
            C = len(grid[0])
            if min(r, c) < 0:
                return 0
            if r >= R or c >= C:
                return 0
            if grid[r][c] == 0:
                return 0
            
            area = 1
            grid[r][c] = 0
            area += findArea(r + 1, c)
            area += findArea(r - 1, c)
            area += findArea(r, c + 1)
            area += findArea(r, c - 1)
            return area
        
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, findArea(r,c))
        
        return maxArea

        