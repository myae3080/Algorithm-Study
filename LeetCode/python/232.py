# source : https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            
        return self.pop_stack.pop()

    def peek(self) -> int:
        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
        
        return self.pop_stack[-1]

    def empty(self) -> bool:
        return False if self.push_stack or self.pop_stack else True