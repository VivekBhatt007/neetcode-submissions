class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return False
        if self.size[p2] > self.size[p1]:
            p1, p2 = p2, p1
        
        self.par[p2] = p1
        self.size[p1] += self.size[p2]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        for idx, e in enumerate(edges):
            e.append(idx)

        edges.sort(key=lambda e: e[2])

        min_cost = 0
        uf = UnionFind(n)
        for n1, n2, w, idx in edges:
            if uf.union(n1, n2):
                min_cost +=w
        
        crit, pesu = [], []
        for n1, n2, e_w, i in edges:
            curr_w = 0
            uf = UnionFind(n)
            for v1, v2, w, j in edges:
                # skip current node
                if i != j and uf.union(v1, v2):
                    curr_w += w
            if max(uf.size) != n or curr_w > min_cost:
                crit.append(i)
                continue
            
            uf = UnionFind(n)
            uf.union(n1, n2)
            curr_w = e_w
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    curr_w += w
            if curr_w == min_cost:
                pesu.append(i)
        return [crit, pesu]
