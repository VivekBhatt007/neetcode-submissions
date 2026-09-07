class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visited = set()
        pq = [[0,0]]
        while len(visited) < N:
            cost, n = heapq.heappop(pq)
            if n in visited:
                continue
            
            res += cost
            visited.add(n)
            for dist, n2 in adj[n]:
                if n2 not in visited:
                    heapq.heappush(pq, [dist, n2])
        return res
        