class MedianFinder:

    def __init__(self):
        # small is max heap which contain max small element
        self.small = []
        # Large is min heap which contain min large element
        self.large = []
        

    def addNum(self, num: int) -> None:
        # first push any number to the small heap
        heapq.heappush(self.small, -1 * num)
        # if top of small heap is larger then top to large heap then remove that
        # from small and add into large
        if self.small and self.large and -self.small[0] > self.large[0]:
            heapq.heappop(self.small)
            heapq.heappush(self.large, num)
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0])/2
        