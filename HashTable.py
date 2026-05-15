class HashTable:
    def __init__(self, init_size = 10):
        self.size = init_size
        self.count = 0
        self.table = [None] * self.size
        return
    
    def calc_hash(self, key):
        total = sum(ord(char) for char in key)
        index = total % self.size 
        if index < 0 or index > self.size:
            return False
        else:
            return index
        
    def insert(self, key, value):
        if self.count > self.size:
            print("Rehash")
        else:
            index = self.calc_hash(key)
            if index is False:
                print("Error Calculating")
                return
            elif self.table[index] is None:
                self.table[index] = (key, value)
            else:
                print("temp")

    def search(self, search_key):
        for item in self.table:
            if item is None:
                continue
            key, value = item
            if search_key is key:
                print(value)
                return
        print("The key is not in the table")
        return


    def print_all(self):
        for item in self.table:
            if item is not None:
                key, value = item
                print(f"{key} and {value}")

    

