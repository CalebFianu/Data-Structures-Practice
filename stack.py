from exceptions import Empty

class ArrayStack:
    def __init__(self):
        self.data = []
    
    def len(self): #for the length of the stack
        return len(self.data)
    
    def isEmpty(self): #checks to see if the stack is empty
        return len(self.data) == 0

    def push(self, e): #where 'e' is the element to be pushed onto the stack
        self.data.append(e)

    def pop(self):
        if self.isEmpty():
            raise Empty('Your stack is Empty')
        return self.data.pop()
    
    def top(self):
        if self.isEmpty():
            raise Empty('Your stack is Empty')
        return self.data[-1]
    
s = ArrayStack()
s.push(10)
s.push(50)
s.push(100)
s.top()
print(s.data)
print('Length of the stack: ', len(s.data))
print('Element popped: ', s.pop())
print('Your current stack: ', s.data)
print('Last element is:', s.top())