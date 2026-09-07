class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        n = numCourses
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)

        topo = []
        visited = set()
        path = set()
        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True
            
            visited.add(c)
            path.add(c)
            for n in adj[c]:
                if not dfs(n):
                    return False
            
            path.remove(c)
            topo.append(c)
            return True
        
        for i in range(n):
            if not dfs(i):
                return []
        return topo

        