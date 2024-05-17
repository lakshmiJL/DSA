class Stack:
    def __init__(self, n):
        self.stack = []
        self.n = n #maximum number of elements in the stack (upto user)

    def push(self, k):
        if len(self.stack) < self.n:
            self.stack.append(k)
        else:
            print("The stack is full.")

    def pop(self):
        if len(self.stack) == 0: # If the stack is empty then pop should do nothing
            print("The stack is empty.")
        else:
            self.stack.pop(-1) # delete the last element and return it
    
    def top(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack) 

    def display(self):
        print(self.stack)


s = Stack(3)
s.display()
print(s.size()) 
s.push(5)
s.display()
print(s.size()) 
s.push(10) 
s.display()
print(s.size()) 
s.push(15)
s.display()
print(s.size()) 
s.push(25)
s.display()
print(s.size()) 
s.pop()
s.display()
print(s.size()) 
print(s.top())