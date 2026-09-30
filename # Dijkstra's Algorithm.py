# Dijkstra's Algorithm

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

graph = [[0] * n for i in range(n)]

print("Enter edges: source destination weight")

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

source = int(input("Enter source vertex: "))

distance = [999999] * n
visited = [False] * n

distance[source] = 0

for i in range(n):

    minimum = 999999
    current = -1

    for j in range(n):
        if not visited[j] and distance[j] < minimum:
            minimum = distance[j]
            current = j

    if current == -1:
        break

    visited[current] = True

    for j in range(n):
        if graph[current][j] != 0 and not visited[j]:

            new_distance = distance[current] + graph[current][j]

            if new_distance < distance[j]:
                distance[j] = new_distance

print("\nShortest distances:")

for i in range(n):
    print(source, "->", i, "=", distance[i])