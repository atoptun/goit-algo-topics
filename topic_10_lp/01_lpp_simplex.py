import pulp


def main():
    prob = pulp.LpProblem("Sample_Problem", pulp.LpMaximize)

    x1 = pulp.LpVariable("x1", lowBound=0)  # x1 >= 0
    x2 = pulp.LpVariable("x2", lowBound=0)  # x2 >= 0

    prob += 3 * x1 + 2 * x2, "Objective"

    prob += 2 * x1 + x2 <= 100, "Constraint_1"
    prob += x1 + x2 <= 80, "Constraint_2"
    prob += x1 <= 40, "Constraint_3"

    prob.solve()

    print("Status:", pulp.LpStatus[prob.status])
    print("Optimal value of x1:", x1.varValue)
    print("Optimal value of x2:", x2.varValue)
    print("Optimal objective value:", pulp.value(prob.objective))


def test_1():
    # model = pulp.LpProblem("Model_Name", pulp.LpMinimize)  # Мінімізація
    # або
    model = pulp.LpProblem("Model_Name", pulp.LpMaximize)  # Максимізація

    x = pulp.LpVariable('x', lowBound=0, cat='Continuous')  # x ≥ 0
    y = pulp.LpVariable('y', 3, 7)        # 3 ≤ y ≤ 7

    model += 2 * x + 3 * y, "Problem"  # Мінімізувати або максимізувати 2x + 3y

    model += x + 2 * y <= 8, "Constraint_1"
    model += y >= 2, "Constraint_2"

    model.solve()

    print("Status:", pulp.LpStatus[model.status])
    for variable in model.variables():
        print(f"Optimal value of {variable.name} = {variable.varValue}")

    # Вартість цільової функції
    print(f"Total cost = {pulp.value(model.objective)}")
 
    # print("Optimal value of x1:", x.varValue)
    # print("Optimal value of x2:", y.varValue)
    # print("Optimal objective value:", pulp.value(model.objective))


def test_2():
    # Ініціалізація моделі
    model = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

    # Визначення змінних
    A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту А
    B = pulp.LpVariable('B', lowBound=0, upBound=10, cat='Integer')  # Кількість продукту Б

    # Функція цілі (Максимізація прибутку)
    model += 50 * A + 40 * B, "Profit"

    # Додавання обмежень
    model += 5 * A + 2 * B <= 80  # Обмеження для машини №1
    model += 3 * A + 2 * B <= 40  # Обмеження для машини №2

    # Розв'язання моделі
    model.solve()

    # Вивід результатів
    print("Виробляти продуктів А:", A.varValue)
    print("Виробляти продуктів Б:", B.varValue)    
    print(f"Total cost = {pulp.value(model.objective)}")


if __name__ == "__main__":
    # main()
    # test_1()
    test_2()