from pprint import pprint


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for ind, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    self.table[key_hash].pop(ind)
                    return True
        return False


def main():
    # Тестуємо нашу хеш-таблицю:
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    H.insert("apple1", 110)
    H.insert("orange1", 120)
    H.insert("banana1", 130)
    H.insert("apple2", 210)
    H.insert("orange2", 220)
    H.insert("banana2", 230)
    pprint(H.table)
    H.delete("apple2")
    pprint(H.table)


    # print(H.get("apple"))   # Виведе: 10
    # print(H.get("orange"))  # Виведе: 20
    # print(H.get("banana"))  # Виведе: 30


if __name__ == '__main__':
   main()