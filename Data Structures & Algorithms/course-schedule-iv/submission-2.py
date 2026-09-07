class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)
        indegree = [0] * numCourses
        preReq = [set() for _ in range(numCourses)]
        for pre, crs in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            n = q.popleft()
            for nei in adj[n]:
                preReq[nei].add(n)

                preReq[nei].update(preReq[n])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return [u in preReq[v] for u, v in queries]


        # adj = defaultdict(list)
        # for src, dst in prerequisites:
        #     adj[src].append(dst)

        # def dfs(i, dst):
        #     if i == dst:
        #         return True
            
        #     for n in adj[i]:
        #         if dfs(n, dst):
        #             return True
        #     return False
        
        # res = []
        # for s, d in queries:
        #     res.append(dfs(s,d))
        # return res
        