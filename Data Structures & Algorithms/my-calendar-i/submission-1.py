class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.right = None
        self.left = None
    
    def insert(self, start, end):
        curr = self
        # if not curr:
        #     curr = TreeNode(start, end)
        #     return True
        while True:
            if start >= curr.end:
                if not curr.right:
                    curr.right = TreeNode(start, end)
                    return True
                curr = curr.right
            elif end <= curr.start:
                if not curr.left:
                    curr.left = TreeNode(start, end)
                    return True
                curr = curr.left
            else:
                return False 

class MyCalendar:
    
    # def __init__(self):
    #     self.events = []

    # def book(self, startTime: int, endTime: int) -> bool:
    #     for s,e in self.events:
    #         if (startTime < e and endTime > s):
    #             return False
    #     self.events.append((startTime, endTime))
    #     return True
    def __init__(self):
        self.root = None

    def book(self, start, end) -> bool:
        if not self.root:
            self.root = TreeNode(start, end)
            return True
        return self.root.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)