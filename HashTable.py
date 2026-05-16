class HashTable:
    def __init__(self, init_size = 10):
        self.size = init_size
        self.count = 0
        self.table = [None] * self.size
        return
    
    def calc_hash(self, key):
        total = sum(ord(char) for char in key)
        index = total % self.size 
        return index
        
    def rehash(self):
        old_table = self.table
        old_size = self.size
        self.size = old_size * 2
        self.table = [None] * self.size
        self.count = 0

        for item in old_table: 
            if item is not None:
                key = item[0]
                value = item[1]
                self.insert(key, value)
        return
    
    def direct_insert(self, key, value):
        index = self.calc_hash(key)
        probe = 0

        while probe < self.size:
            item = self.table[index]
            if item is None:
                self.table[index] = (key, value)
                self.count += 1
                return
            elif item[0] == key:
                self.table[index] = (key, value)
                return
            else:
                index = (index + 1) % self.size
                probe += 1

    
    def indexError(self):
        print(f"index < 0 or index > {self.size}")
        
    def insert(self, key, value):
        load_factor = self.count / self.size
        if load_factor > 0.7:
            self.rehash()
        
        index = self.calc_hash(key)
        
        while True:
            item = self.table[index]
            if item is None:
                self.table[index] = (key, value)
                self.count += 1
                return
            elif item[0] == key:
                self.table[index] = (key, value)
                return
            else:
                index = (index + 1) % self.size

    def search(self, search_key):
        if self.table is None:
            print("Table is empty")
            return
        
        index = self.calc_hash(search_key)
        if index < 0 or index > self.size:
            self.indexError()
            return
        
        probe = 0
        
        while True and probe < len(self.table):
            if self.table[index] is None:
                print("Not found")
                return
            elif self.table[index][0] == search_key:
                print(f"Found {self.table[index][1]}")
                return
            else:
                index = (index + 1) % len(self.table) #probe
                probe += 1
        print("Key is not in the table")

    def delete(self, delete_key):
        if self.table is None:
            print("Table is empty")
            return
        
        index = self.calc_hash(delete_key)
        if index < 0 or index > self.size:
            self.indexError()
            return
        probe = 0

        while True and probe < len(self.table):
            if self.table[index] is None:
                print("Key is not in the table")
                return
            elif self.table[index][0] == delete_key:
                self.table[index] = ("DELETED", "DELETED")
                self.count -= 1
                print(f"{delete_key} successfully deleted")
                return
            else:
                index = (index + 1) % self.size
                probe += 1
        #if not found
        print("Key is not in the table")

    def print_all(self):
        for item in self.table:
            if item is not None:
                key, value = item
                print(f"{key} and {value}")

    

