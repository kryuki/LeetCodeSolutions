class MyQueue:
    #solution1: two stacks
    #time: O(1), space: O(1)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []
        
    #time: O(1), space: O(n)
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)
    
    #time: Amortized O(1), Worst-case O(n), space: O(1) 
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.outStack:
            self.move()
        return self.outStack.pop()
        
    #time: Amortized O(1), Worst-case O(n), space: O(1)
    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.outStack:
            self.move()
        return self.outStack[-1]
        
    #time: O(1), space: O(1)
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inStack and not self.outStack
    
    def move(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()