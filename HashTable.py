class HashTable:
    def __init__(self, init_size = 10):
        self.size = init_size
        self.count = 0
        self.table = [None] * self.size
        return
    
    def calc_hash(self, key):
        total = sum(ord(char) for char in key)
        index = total / self.size 
        if index < 0 or index > self.size():
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


    def print_all(self):
        for key, value in self.list:
            if key and value is not None:
                print(f"{key} and {value}")

    

