import random

def is_inside(a, b, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= (b / a) * x

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

        # Розрахунок площі за методом Монте-Карло
        M = len(inside_points)
        N = len(points)
        area = (M / N) * (a * b)

        # Додавання до середньої площі
        average_area += area

    # Обчислення середньої площі
    average_area /= num_experiments
    return average_area

# Розміри прямокутника
a = 10  # ширина прямокутника
b = 5  # висота прямокутника
S = (a * b) / 2  # Теоретична площа

# Кількість експериментів
num_experiments = 100

# Виконання симуляції
average_area = monte_carlo_simulation(a, b, num_experiments)
print(f"Теоретична площа трикутника: {S}")
print(f"Середня площа трикутника за {num_experiments} експериментів: {average_area}")
print(f"Похибка: {abs(S - average_area)}")