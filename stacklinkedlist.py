class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
    
    def pop(self):
        if self.head == None:
            return None
        else: popped = self.head
        self.head = self.head.next
        return popped.val

    def peek(self):
        if self.head == None:
            return None
        else: 
            return self.head.val

class MinStack:
    def __init__(self):
        self.items = []
        self.mins = []

    def push(self, val):
        self.items.append(val)
        if(len(self.mins) == 0):
            self.mins.append(val)
        else:
            self.mins.append(min(val, self.getMin()))

    def pop(self):
        self.items.pop()
        self.mins.pop()

    def peek(self):
        return self.items[-1]

    def getMin(self):
        return self.mins[-1]

def main():

    #valid parantheses problem
    def is_valid(s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if (len(stack) == 0):
                    return False
                stack.pop()
        return len(stack) == 0

    s = '((()))'
    print(is_valid(s))


main()