import matplotlib.pyplot as plt
import numpy as np

# Визначаємо кількість елементів та відповідні кроки для лінійного та двійкового пошуку
n = np.arange(1, 21)
linear_search_steps = n
binary_search_steps = np.log2(n)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(n, linear_search_steps, label='Linear Search', color='blue')
plt.plot(n, binary_search_steps, label='Binary Search', color='green')
plt.xlabel('Number of elements (n)')
plt.ylabel('Number of steps')
plt.title('Comparison of Linear and Binary Search')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Відображення графіка
plt.show()
