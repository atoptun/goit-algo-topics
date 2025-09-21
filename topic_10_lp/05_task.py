"""
x1 - Limonade: water - 2, sugar - 1, lemon juice - 1.
x2 - Fruit juice: water - 1, fruit puree - 2.

Resources available:
    water - 100
    sugar - 50 
    lemon juice - 30
    fruit puree - 40

Max profit: Z = x1 + x2

Limits:
    2*x1 + x2 <= 100
    x1 <= 50
    x1 <= 30
    2*x2 <= 40
    x1 >= 0
    x2 >= 0
"""

import pulp


def max_profit():
    model = pulp.LpProblem("Maximize_Products", pulp.LpMaximize)

    x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
    x2 = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

    model += x1 + x2, "Total_Products"

    model += 2*x1 + x2 <= 100, "Water_Constraint"
    model += x1 <= 50, "Sugar_Constraint"
    model += x1 <= 30, "Lemon_Juice_Constraint"
    model += 2*x2 <= 40, "Fruit_Puree_Constraint"

    model.solve()

    # Вивід результатів
    print("Status:", pulp.LpStatus[model.status])
    for var in model.variables():
        print(f"Optimal value of {var.name} = {var.value()}")
    print("Optimal objective value:", pulp.value(model.objective))


if __name__ == "__main__":
    max_profit()
