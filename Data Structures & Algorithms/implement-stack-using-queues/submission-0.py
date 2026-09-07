class MyStack:

    def __init__(self):
        self.dque = deque()
        

    def push(self, x: int) -> None:
        self.dque.append(x)
        

    def pop(self) -> int:
        return self.dque.pop()

    def top(self) -> int:
        return self.dque[-1]
        

    def empty(self) -> bool:
        return len(self.dque) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()