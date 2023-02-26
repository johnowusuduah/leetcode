#Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack 
#(push, top, pop, and empty).

#Implement the MyStack class:
#void push(int x) Pushes element x to the top of the stack.
#int pop() Removes the element on the top of the stack and returns it.
#int top() Returns the element on the top of the stack.
#boolean empty() Returns true if the stack is empty, false otherwise.

#Notes:
#You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
#Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long 
#as you use only a queue's standard operations.

from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # we will refrain from using the methods associated with queues
        # move every element but the last element we want to pop to the back of the
        # que so that the last element will be the first our (LIFO) as stated in the question
        
        n = len(self.q) - 1
        for _ in range(n):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
