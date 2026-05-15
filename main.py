from HashTable import HashTable
def main():
    hashTable = HashTable()
    hashTable.insert("Sydney", "1")
    hashTable.insert("Melbourne", "2")
    hashTable.print_all()
    hashTable.search("Melbourne")
    hashTable.delete("Melbourne")
    hashTable.print_all()
    return


if __name__ == "__main__":
    main()
