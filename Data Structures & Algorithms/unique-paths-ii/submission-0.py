class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[R-1][C-1] == 1:
            return 0
        cache = [[0] * (C+1) for _ in range(R+1)]
        cache[R-1][C-1] = 1

        for r in range(R-1, -1, -1):
            for c in range(C-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    cache[r][c] = 0
                else:
                    cache[r][c] += cache[r+1][c] + cache[r][c+1]
        
        return cache[0][0]

        # prev_row = [0] * (C +1)

        # for r in range(R-1, -1 , -1):
        #     curr_row = [0] * C
        #     curr_row[C-1] = 1
        #     for c in range(C-1, -1, -1):
        #         if obstacleGrid[r][c] == 1:
        #             curr_row[c] = 0
        #         elif c+1 == C:
        #             curr_row[c] = 0 + prev_row[c]
        #         else:
        #             curr_row[c] = curr_row[c+1] + prev_row[c]
        #     print(f"row idx: {r}: {curr_row}")
        #     prev_row = curr_row

        # return curr_row[0]


        