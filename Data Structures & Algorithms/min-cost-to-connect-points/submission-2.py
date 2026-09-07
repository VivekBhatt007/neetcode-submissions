class UF:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * (n)
    
    def find(self, x):
        while self.parents[x] != x:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return self.parents[x]
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        
        if self.size[p2] > self.size[p1]:
            p1, p2 = p2, p1

        self.parents[p2] = p1
        self.size[p1] += self.size[p2]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append([dist, i, j])
        
        edges.sort()
        uf = UF(n)
        res = 0
        for d, n1, n2 in edges:
            if uf.union(n1,n2):
                res += d
        return res

        