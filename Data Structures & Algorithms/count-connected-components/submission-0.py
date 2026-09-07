

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
        
        def union(n1, n2):
            nonlocal component
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return
            
            component -= 1
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return
        
        for e in edges:
            union(e[0], e[1])
        
        return component
        