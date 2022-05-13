class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val, end = " ")
            temp = temp.next
    
    def insert_beginning(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

if __name__ =='__main__':
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    new_node = Node(0)

    llist.head.next = second
    second.next = fourth
    fourth.next = third
    llist.insert_beginning(0)

    llist.printList()