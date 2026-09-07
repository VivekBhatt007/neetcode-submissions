class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visited = set()
        minpq = [[grid[0][0], 0, 0]]
        dire = [[0,1], [0,-1], [1,0], [-1,0]]
        visited.add((0,0))

        while minpq:
            t, r, c = heapq.heappop(minpq)

            if r == N -1 and c == N - 1:
                return t
            
            for dr, dc in dire:
                nr, nc = r +dr , c + dc
                if ( nr < 0 or nc < 0 or
                    nr >= N or nc >= N or (nr, nc) in visited):
                    continue
                
                visited.add((nr, nc))
                heapq.heappush(minpq, [max(t, grid[nr][nc]), nr, nc])
        
        return -1
        