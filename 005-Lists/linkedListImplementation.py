class LinkedList:
    class Node:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev

    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def add_to_head(self, value):
        new_node = self.Node(value)
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node

    def add_to_tail(self, value):
        new_node = self.Node(value)
        if self.back is None:
            self.front = new_node
            self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node

    def remove_from_head(self):
        if self.front is None:
            return None
        value = self.front.value
        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            self.front.prev = None
        return value

    def remove_from_tail(self):
        if self.back is None:
            return None
        value = self.back.value
        if self.front == self.back:
            self.front = None
            self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None
        return value

    def search(self, value):
        current = self.front
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def remove(self, value):
        current = self.front
        while current:
            if current.value == value:
                if current == self.front:
                    self.remove_from_head()
                elif current == self.back:
                    self.remove_from_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return True
            current = current.next
        return False


# Example usage:

ll = LinkedList()
ll.add_to_head(3)
ll.add_to_head(2)
ll.add_to_head(1)

ll.add_to_tail(4)
ll.add_to_tail(5)

print(ll.search(3))  # Output: True
print(ll.search(6))  # Output: False

ll.remove(3)
ll.remove_from_tail()

currNode = ll.front
while currNode:
    print(currNode.value)
    currNode = currNode.next