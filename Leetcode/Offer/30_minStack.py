# Build a stack structure to return minimum.

class Solution:
    def __init__(self):
        self.A = []
        self.B = []


    def push(self, x):
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self):
        if self.B[-1] == self.A.pop():
            self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]