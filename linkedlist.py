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

def merge(l1, l2):
#Using the dummy node technique
    dummy = Node(0)
    current = dummy

    while(l1 != None and l2 != None ):
        if l1.val < l2.val:
            current.next = Node(l1.val)
            l1 = l1.next
        else:
            current.next = Node(l2.val)
            l2 = l2.next
        current = current.next
    
    #For any leftover nodes
    while(l1 != None):
        current.next = Node(l1.val)
        l1 = l1.next
    while(l2 != None):
        current.next = Node(l2.val)
        l2 = l2.next


if __name__ =='__main__':
    llist = LinkedList()
    new_list = LinkedList()

    llist.head = Node(1)
    second = Node(3)
    third = Node(5)
    new_node = Node(0)

    new_list.head = Node(2)
    new_sec = Node(4)

    llist.head.next = second
    second.next = third
    #llist.insert_beginning(0)

    #llist.printList()
    print()