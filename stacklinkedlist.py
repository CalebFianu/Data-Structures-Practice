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