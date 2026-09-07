class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for edge, sp in zip(edges, succProb):
            src, dst = edge
            adj[src].append((dst, sp))
            adj[dst].append((src, sp))
        
        heap = [(-1.0, start_node)]
        seen = {}
        while heap:
            p1, n1 = heapq.heappop(heap)
            if n1 in seen:
                continue
            seen[n1] = -p1

            for n2, p2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(heap, (-(-p1*p2), n2))
        
        return seen.get(end_node, 0.0)


        