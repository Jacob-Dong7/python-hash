from HashTable import HashTable

def testing():
    ht = HashTable(10)
    print("\n1. Testing Insert:")
    ht.insert("Sydney", "New South Wales")
    ht.insert("Melbourne", "Victoria")
    ht.insert("Brisbane", "Queensland")
    ht.insert("Perth", "Western Australia")
    
    print("\n2. Testing print_all():")
    ht.print_all()
    
    print("\n3. Testing search():")
    ht.search("Melbourne")
    ht.search("Sydney")
    ht.search("Adelaide")       
    
    print("\n4. Testing delete():")
    ht.delete("Melbourne")
    print("After delete Melbourne:")
    ht.print_all()
    
    print("\n5. Testing calc_hash():")
    print("Hash of 'Sydney':", ht.calc_hash("Sydney"))
    print("Hash of 'ABC':", ht.calc_hash("ABC"))
    
    print("\n6. Testing Rehash (force by adding many items):")
    for i in range(12):                
        ht.insert(f"Key{i}", f"Value{i}")
    print("\nAfter rehash triggered:\n")
    ht.print_all()
    
    print("\n7. Testing search after rehash:")
    ht.search("Key5")
    
    print("\n8. Testing table_empty (manual check):")
    if ht.count == 0:
        ht.table_empty()
    else:
        print("Table is NOT empty, count =", ht.count)

if __name__ == "__main__":
    testing()