import random

def is_prime(n, k=5):  # k - кількість ітерацій
    # Rabin–Miller primality test
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True

    # Знаходимо r та d
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Проводимо k тестів
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    # Приклад використання:
    n = 561  # Число Кармайкла
    print(is_prime(n))  # поверне False, хоча 561 - псевдопросте число
