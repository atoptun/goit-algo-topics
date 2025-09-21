# https://uk.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%BF%D0%B0%D0%BA%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F_%D1%80%D1%8E%D0%BA%D0%B7%D0%B0%D0%BA%D0%B0

# Функція для обчислення максимальної вартості
def knapSack(W, wt, val, n):
    # повним перебором.
    # часова складність є експоненційною
    # O(2^n), де n — кількість предметів.

    # Базовий випадок
    if n == 0 or W == 0:
        return 0

    # Якщо вага n-го предмета більше, ніж місткість рюкзака, то цей предмет не можна включити у рюкзак
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)

    # повертаємо максимум із двох випадків:
    # (1) n-ий предмет включено
    # (2) не включено
    else:
        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1),
        )

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# викликаємо функцію
print(knapSack(capacity, weight, value, n))  # 220


# ==============

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def knapSack2(items: list[Item], capacity: int) -> int:
    # жадібний підхід
    # загальна часова складність нашого жадібного алгоритму не лінійна, 
    # а буде визначена часом, необхідним для сортування, і становитиме
    # O(n log n + n) спрощується до O(n log n)

    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
    return total_value

# Дані предметів
items = [Item(10, 60), Item(20, 100), Item(30, 120)]
# Місткість рюкзака
capacity = 50
# Виклик функції
print(knapSack2(items, capacity))  # 160

# ==============

def knapSack3(W, wt, val, n):
    # динамічне програмування
    # часова складність O(n*W), де n — кількість предметів,
    # а W — місткість рюкзака.
    # простір складність також O(n*W) для зберігання таблиці.

    # створюємо таблицю K для зберігання оптимальних значень підзадач
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# виклик функції
print(knapSack3(capacity, weight, value, n))  # 220
