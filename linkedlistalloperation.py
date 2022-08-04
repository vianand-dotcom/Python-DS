class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def traverseinlist(self):
        traverse = llist.head
        while traverse != None:
            print(traverse.data)
            traverse = traverse.next

    def lengthoflist(self):
        traverse = llist.head
        if self.checkemptylist():
            return 0
        else:
            length = 0
            while traverse != None:
                # print(traverse.data)
                traverse = traverse.next
                length += 1
            return length

    def checkemptylist(self):
        if self.head == None:
            return True
        else:
            return False

    def insertatbeg(self, data):
        node = Node(data)
        if self.checkemptylist():
            print(f'List is empty adding {node.data} in the beginning')
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insertatspecific(self, data, pos):
        if pos > self.lengthoflist():
            print(
                f'List is short\n size of list is {self.lengthoflist()} \n Position you specified is {pos}')
        # node = Node(data)
        elif self.checkemptylist():
            self.insertatbeg(data)
        else:
            i = 1
            node = Node(data)
            traverse = self.head
            while i < pos-1:
                traverse = traverse.next
                i += 1
            node.next = traverse.next
            traverse.next = node

    def insertatend(self, data):
        node = Node(data)
        if self.checkemptylist():
            print(f'List is empty adding {node.data} in the beginning')
            self.head = node
        else:
            traverse = self.head
            while traverse.next != None:
                traverse = traverse.next
            traverse.next = node

    def deleteatspecific(self, pos):
        if self.lengthoflist() < pos:
            print(
                f'Length of list {self.lengthoflist()} is smaller than the position {pos} you passed')
        elif pos == 1:
            self.deletefrombeg()
        elif pos == self.lengthoflist():
            self.deletefromend()
        else:
            traverse = self.head
            i = 1
            while i < pos:
                traverse = traverse.next
                i += 1
                if i == pos-1:
                    temp = traverse
            temp.next = traverse.next
            traverse.next = None

    def deletefrombeg(self):
        traverse = self.head
        self.head = traverse.next
        traverse.next = None

    def deletefromend(self):
        traverse = self.head
        while traverse.next != None:
            temp = traverse
            traverse = traverse.next
        temp.next = None


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(4)
    second = Node(5)
    third = Node(6)

llist.head.next = second
second.next = third
llist.traverseinlist()
llist.insertatbeg(28)
print("After insertion at beg")
llist.traverseinlist()
print("After insertion at specific position")
llist.insertatspecific(32, 3)
llist.traverseinlist()
print("After inserting at the end of list")
llist.insertatend(99)
llist.traverseinlist()

print(f'before deleting from specific location')
llist.traverseinlist()
llist.deleteatspecific(3)
print(f'After deleting from specific location')
llist.traverseinlist()
llist.deletefrombeg()
print("After deleting from beginning")
llist.traverseinlist()
llist.deletefromend()
print("After deleting from end")
llist.traverseinlist()
