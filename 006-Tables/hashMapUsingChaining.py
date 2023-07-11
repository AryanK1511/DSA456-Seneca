class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None or self.table[index].key == key:
            self.table[index] = Node(key, value)
            return
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current = Node(key, value)
                current = current.next
            current.next = Node(key, value)

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return
        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            return
        curr = self.table[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def search(self, key):
        index = self.hash_function(key)
        curr = self.table[index]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

hash_map = HashTable(20)
hash_map.insert("A", "Apple")
hash_map.insert("B", "Ball")
hash_map.insert("C", "Cat")
hash_map.insert("D", "Dog")
hash_map.insert("D", "Daaru")
print(hash_map.search("C"))
print(hash_map.search("D"))
hash_map.delete("D")
print(hash_map.search("D"))