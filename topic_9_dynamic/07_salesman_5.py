from heapq import heappush, heappop
import networkx as nx


# https://uk.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D0%9F%D1%80%D0%B8%D0%BC%D0%B0
# Алгоритм Прима
# часова складність O(E log V), де E - кількість ребер, V - кількість вершин

def prim_mst(graph):
  # Створення порожнього МОД
  mst = nx.Graph()

  # Відвідані вершини, починаючи з випадкової початкової вершини
  visited = {list(graph.nodes())[0]}

  # Черга з пріоритетами для ребер, яка ініціалізується ребрами початкової вершини
  edges = []
  for _, v, weight in graph.edges(data='weight', nbunch=visited):
    heappush(edges, (weight, _, v))

  # Поки в МОД не всі вершини
  while visited != set(graph.nodes()):
    # Вибираємо ребро з найменшою вагою, що з'єднує дерево з новою вершиною
    weight, u, v = heappop(edges)
    if v not in visited:
      # Додаємо нову вершину до МОД
      visited.add(v)
      mst.add_edge(u, v, weight=weight)
      # Додаємо всі ребра з нової вершини до черги з пріоритетами
      for _, new_v, new_weight in graph.edges(data='weight', nbunch=[v]):
        if new_v not in visited:
          heappush(edges, (new_weight, v, new_v))

  return mst


# Створення графа для демонстрації
G = nx.Graph()
G.add_edge('A', 'B', weight=7)
G.add_edge('A', 'D', weight=5)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'D', weight=9)
G.add_edge('B', 'E', weight=7)
G.add_edge('C', 'E', weight=5)
G.add_edge('D', 'E', weight=15)
G.add_edge('D', 'F', weight=6)
G.add_edge('E', 'F', weight=8)
G.add_edge('E', 'G', weight=9)
G.add_edge('F', 'G', weight=11)

# Виконання алгоритму Прима на графі G
mst = prim_mst(G)

# Виведення ребер мінімального остовного дерева
print("Edges in the MST:")
for edge in mst.edges(data=True):
  print(edge)