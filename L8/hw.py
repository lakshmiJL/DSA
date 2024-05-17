class StackUsingQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self, element):
        self.queue1.append(element)
    
    def pop(self):
        if not self.queue1:
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        popped_element = self.queue1.pop(0)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_element

    def top(self):
        if not self.queue1:
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        
        top_element = self.queue1[0]
        
        self.queue2.append(self.queue1.pop(0))
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_element

    def empty(self):
        return len(self.queue1) == 0

# Example usage
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # Output: 3
print(stack.top())  # Output: 2
print(stack.empty())  # Output: False
