from collections import deque

def topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    for u in graph: [in_degree.update({v: in_degree[v] + 1}) for v in graph[u]]
    queue, topo_order = deque([u for u in graph if in_degree[u] == 0]), []
    while queue:
        u = queue.popleft(); topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0: queue.append(v)
    return topo_order

graph = {0: [1], 1: [2], 2: [3], 3: []}
print(topological_sort(graph))  # Output: [0, 1, 2, 3]
