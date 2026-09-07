
from collections import defaultdict

class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        eToA = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in eToA:
                    uf.union(i, eToA[e])
                else:
                    eToA[e] = i
        
        eGroup = defaultdict(list)
        for e, i in eToA.items():
            l = uf.find(i)
            eGroup[l].append(e)
        
        res = []
        for idx, emails in eGroup.items():
            n = accounts[idx][0]
            res.append([n] + sorted(emails))
        return res
        