

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n
        component = n

        def find(x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        
        def union(n1, n2) -> bool:
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True
        
        for e in edges:
            if union(e[0], e[1]):
                component -= 1
        
        return component
        