import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            dist = math.sqrt(point[0]*point[0] + point[1]*point[1])
            heapq.heappush(maxHeap, (-dist, point))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for tup in maxHeap:
            res.append(tup[-1])
        return res
        
        