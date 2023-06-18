class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.front = self.Node(None)
        self.back = self.Node(None, None, self.front)
        self.front.next = self.back

    def push_front(self, value):
        nn = self.Node(value)
        nn.next = self.front.next
        nn.prev = self.front
        self.front.next.prev = nn
        self.front.next = nn

    def push_back(self, value):
        nn = self.Node(value)
        nn.prev = self.back.prev
        nn.next = self.back
        self.back.prev.next = nn
        self.back.prev = nn

    def pop_front(self):
        if self.front.next is not self.back:
            rm = self.front.next
            self.front.next = rm.next
            rm.next.prev = self.front
            del rm

    def pop_back(self):
        if self.back.prev is not self.front:
            rm = self.back.prev
            self.back.prev = rm.prev
            rm.prev.next = self.back
            del rm

    def printLL(self):
        curr = self.front.next
        while curr is not self.back:
            print(curr.data)
            curr = curr.next

ll = LinkedList()
ll.push_front(10)
ll.push_front(20)
ll.push_back(30)
ll.push_back(40)
ll.printLL()
ll.pop_front()
ll.pop_back()
ll.printLL()
