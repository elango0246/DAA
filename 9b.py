from itertools import permutations

def tsp(graph):
    n = len(graph)
    vertices = list(range(1, n))
    min_cost = float('inf')
    best_path = []

    for perm in permutations(vertices):
        current_cost = 0
        k = 0
        for j in perm:
            current_cost += graph[k][j]
            k = j
        current_cost += graph[k][0]  # Returning to the starting point
        if current_cost < min_cost:
            min_cost = current_cost
            best_path = [0] + list(perm) + [0]

    return min_cost, best_path

graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]

cost, path = tsp(graph)
print(f"Minimum Cost: {cost}")
print(f"Path: {path}")
