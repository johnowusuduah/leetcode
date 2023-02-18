#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the MinStack class:
#MinStack() initializes the stack object.
#void push(int val) pushes the element val onto the stack.
#void pop() removes the element on the top of the stack.
#int top() gets the top element of the stack.
#int getMin() retrieves the minimum element in the stack.

#You must implement a solution with O(1) time complexity for each function.

class MinStack:
    def __init__(self):
        self.stack = []
        # will always point to the minimum element
        self.curmin = float('inf')
        # will always store the previous minimum elements
        self.prevmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # this allows us to keep track of elements that are less than the current min. this will not run if the element being pushed is greater than current min.
        if val <= self.curmin:
            self.prevmin.append(self.curmin)
            self.curmin = val

    def pop(self) -> None:
        # if current min is at the front of the stack
        if self.stack[-1] == self.curmin:
            self.curmin = self.prevmin.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curmin