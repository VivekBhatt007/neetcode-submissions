class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def bfsHelper(q, fresh) -> int:
            R = len(grid)
            C = len(grid[0])
            visited = set()
            mins = 0
            while q and fresh > 0:
                ql = len(q)
                for _ in range(ql):
                    c_r, c_c = q.popleft()

                    dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                    for r, c in dirs:
                        nr = c_r + r
                        nc = c_c + c
                        if (min(nr,nc) < 0 or
                            nr >= R or nc >= C or
                            (nr,nc) in visited or grid[nr][nc] == 0 or
                            grid[nr][nc] == 2):
                            continue
                        fresh -= 1
                        q.append((nr,nc))
                        visited.add((nr,nc))
                mins += 1
            return mins if fresh == 0 else -1
        


        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        
        return bfsHelper(q, fresh)


        