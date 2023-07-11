class Table:
    def __init__(self):
        self.table = []

    def insert(self, key, value):
        # Find the insertion point using binary search
        low = 0
        high = len(self.table) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.table[mid][0] == key:
                # Key already exists, update the value
                self.table[mid] = (key, value)
                return
            elif self.table[mid][0] < key:
                low = mid + 1
            else:
                high = mid - 1

        # Key does not exist, insert the new record
        self.table.insert(low, (key, value))

    def remove(self, key):
        # Find the record using binary search
        low = 0
        high = len(self.table) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.table[mid][0] == key:
                # Key found, remove the record
                del self.table[mid]
                return
            elif self.table[mid][0] < key:
                low = mid + 1
            else:
                high = mid - 1

    def search(self, key):
        # Binary search for the record
        low = 0
        high = len(self.table) - 1

        while low <= high:
            mid = (low + high) // 2
            if self.table[mid][0] == key:
                # Key found, return the corresponding value
                return self.table[mid][1]
            elif self.table[mid][0] < key:
                low = mid + 1
            else:
                high = mid - 1

        # Key not found
        return None
