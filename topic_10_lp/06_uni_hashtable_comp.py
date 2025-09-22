import random
from collections import defaultdict


class NaiveHashTable:
    def __init__(self, m):
        self.m = m
        self.table = defaultdict(list)

    def insert(self, key):
        idx = key % self.m
        self.table[idx].append(key)

    def __str__(self):
        return "\n".join(f"{i}: {self.table[i]}" for i in range(self.m))


class UniversalHashTable:
    def __init__(self, m: int, p: int = 10**9+7):
        self.m = m
        self.p = self._next_prime(p)
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)
        self.table = defaultdict(list)

    def _next_prime(self, num: int) -> int:
        """Перевіряє число num на простоту. Повертає наступне просте число після num."""
        while not self._is_prime(num):
            num += 1
        return num

    def _is_prime(self, num: int, k: int = 40) -> bool:
        """Тест Міллера–Рабіна для перевірки простоти числа num."""
        if num == 2:
            return True
        if num % 2 == 0 or num == 1:
            return False
        
        s, d = 0, num - 1
        while d % 2 == 0:
            s += 1
            d //= 2
        for _ in range(k):
            a = random.randint(2, num - 2)
            x = pow(a, d, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(s - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True

    def h(self, x: int) -> int:
        """Хеш-функція для ключа x."""
        return ((self.a * x + self.b) % self.p) % self.m

    def insert(self, key: int):
        """Вставляє ключ у хеш-таблицю."""
        idx = self.h(key)
        self.table[idx].append(key)

    def __str__(self):
        """Повертає рядкове представлення хеш-таблиці."""
        return "\n".join(f"{i}: {self.table[i]}" for i in range(self.m))


# Параметри
m = 10  # розмір хеш-таблиці
keys = [i * 10 for i in range(20)]  # спеціально беремо кратні 10

# Наївне хешування
naive_ht = NaiveHashTable(m)
for k in keys:
    naive_ht.insert(k)

print("=== Наївна хеш-таблиця (x % m) ===")
print(naive_ht)

# Універсальне хешування
universal_ht = UniversalHashTable(m)
for k in keys:
    universal_ht.insert(k)

print("\n=== Універсальна хеш-таблиця ===")
print(universal_ht)
