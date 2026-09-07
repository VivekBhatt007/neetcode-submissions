class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        c_p = sorted(zip(capital, profits))
        max_p = []
        curr_w = w
        idx = 0
        for _ in range(k):
            while idx < len(c_p) and c_p[idx][0] <= curr_w:
                heapq.heappush(max_p, -c_p[idx][1])
                idx += 1
            
            if max_p:
                curr_w += -heapq.heappop(max_p)
            else:
                break
        return curr_w
        