def floyd_warshall(graph):

    n = len(graph)
    # Initialize the distance matrix
    dist = [[999] * n for _ in range(n)]

    # Copy the input graph into the distance matrix
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    # Perform Floyd-Warshall algorithm
    for k in range(n):  # Intermediate node
        for i in range(n):  # Source node
            for j in range(n):  # Destination node
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


# Input graph where '999' represents infinity
graph = [[0, 3, 999, 7],
         [8, 0, 2, 999],
         [5, 999, 0, 1],
         [2, 999, 999, 0]]

# Run the Floyd-Warshall algorithm and print the shortest distance matrix
result = floyd_warshall(graph)
for row in result:
    print(row)
