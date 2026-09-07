class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for time in times:
            ui, vi, ti = time
            adj[ui].append((vi, ti))
        
        seen = {}
        heap = [(0,k)]
        t = 0
        while heap:
           ti, n1 = heapq.heappop(heap)
           if n1 in seen:
               continue
           seen[n1] = ti
           t = ti

           for n2, ti2 in adj[n1]:
               if n2 not in seen:
                   heapq.heappush(heap, (ti+ti2, n2))
        return t if len(seen) == n else -1
            


         
        