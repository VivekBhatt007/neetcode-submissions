class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = {i: [] for i in range(numCourses)}
        for l in prerequisites:
            adjList[l[0]].append(l[1])
        
        visited = set()
        def dfs(course) -> bool:
            if course in visited:
                return False
            
            if adjList[course] == []:
                return True
            visited.add(course)

            for n in adjList[course]:
                if not dfs(n):
                    return False
            
            visited.remove(course)
            adjList[course] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
