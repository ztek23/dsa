class Stack:
    def __init__(self,max):
        self.stack = []
        self.max = max

    def push(self,receive):
        if len(self.stack) < self.max:
            self.stack.append(receive)
        else:
            print("Stack is full")
    
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            self.stack.pop(-1)

    def display(self):
        print(self.stack)

    def size(self):
        print(len(self.stack))

    def top(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print(self.stack[-1])


s1 = Stack(10)
s1.display()
s1.push(9)
s1.push(5)
s1.display()
s1.top()
s1.display()