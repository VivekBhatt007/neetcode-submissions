class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def bfs(grid) -> int:
            R = len(grid)
            C = len(grid[0])
            if grid[0][0] == 1:
                return -1
            visit = set()
            q = deque()
            q.append((0,0))
            visit.add((0,0))
            length = 1
            while q:
                ql = len(q)
                for i in range(ql):
                    cr, cc = q.popleft()
                    if cr == R - 1  and cc == C - 1:
                        return length

                    d = [[0, 1],[0, -1],[1, 0],[-1, 0],[1,1],[1,-1],[-1,1],[-1,-1]]
                    for r,c in d:
                        nr = cr + r
                        nc = cc + c
                        if (min(nr,nc) < 0 or
                            nr >= R or nc >= C or
                            (nr, nc) in visit or grid[nr][nc] == 1):
                            continue
                        q.append((nr,nc))
                        visit.add((nr,nc))
                length += 1
            return -1
        
        return bfs(grid)



        