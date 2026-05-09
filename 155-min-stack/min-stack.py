class MinStack:

    def __init__(self):
        self.stack=[]
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        n=len(self.stack)
        min=float('inf')
        for i in range(n):
            if self.stack[i]<min:
                min=self.stack[i]
        return min
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()