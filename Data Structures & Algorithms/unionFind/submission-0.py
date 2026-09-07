class UnionFind:
    
    def __init__(self, n: int):
        self.parent = {}
        self.rank = 0
        self.comp = n
        for i in range(n):
            self.parent[i] = i
            self.rank = 0 
        

    def find(self, x: int) -> int:
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return True
        return False


    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)
        if p1 == p2:
            return False
        self.comp -= 1
        if self.parent[p1] > self.parent[p2]:
            self.parent[p2] = p1
        elif self.parent[p1] < self.parent[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] +=1
        return True
        

    def getNumComponents(self) -> int:
        return self.comp

