class MinStack:

    def __init__(self):
        # self.st = []
        # self.minSt = []
        self.st = []
        self.min = float('inf')
        

    def push(self, val: int) -> None:
        # self.st.append(val)
        # val = min(val, self.minSt[-1] if self.minSt else val)
        # self.minSt.append(val)
        if not self.st:
            self.st.append(0)
            self.min = val
        else:
            self.st.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        # self.st.pop()
        # self.minSt.pop()
        val = self.st.pop()
        if val < 0:
            self.min = self.min - val
        

    def top(self) -> int:
        # return self.st[-1]
        top = self.st[-1]
        if top > 0:
            top = top + self.min
        else:
            top = self.min
        return top

    def getMin(self) -> int:
        # return self.minSt[-1]
        return self.min
        
