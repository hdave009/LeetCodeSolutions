# https://leetcode.com/problems/min-stack/submissions/

class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not len(self.min) or val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min[-1]:
            self.min.pop()
        return popped

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
