# https://uk.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%A4%D0%BB%D0%BE%D0%B9%D0%B4%D0%B0_%E2%80%94_%D0%92%D0%BE%D1%80%D1%88%D0%B5%D0%BB%D0%BB%D0%B0

# Алгоритм Флойда-Воршелла
# часова складність O(n^3)

def floyd_warshall(graph):
    # Кількість вершин у графі
    n = len(graph)
    
    # Ініціалізація матриці відстаней
    distance = [[float('inf')] * n for _ in range(n)]
    
    # Заповнення діагоналі нулями (відстань від вершини до самої себе)
    for i in range(n):
        distance[i][i] = 0
    
    # Заповнення матриці відстаней вагами ребер
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    
    # Оновлення матриці відстаней
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

# матриця суміжності, де 0 означає відсутність ребра між вершинами
graph = [
    [0, 3, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 7, 0, 2],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 3],
    [0, 0, 0, 0, 0, 0]
]

distance_matrix = floyd_warshall(graph)
for row in distance_matrix:
    print(row)

