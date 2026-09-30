# Prim's Algorithm

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

graph = [[0] * n for i in range(n)]

print("Enter edges: source destination weight")

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

visited = [False] * n
visited[0] = True

total = 0

print("\nEdges in MST:")

for i in range(n - 1):

    minimum = 999999
    x = -1
    y = -1

    for u in range(n):
        if visited[u]:
            for v in range(n):
                if graph[u][v] != 0 and not visited[v]:
                    if graph[u][v] < minimum:
                        minimum = graph[u][v]
                        x = u
                        y = v

    print(x, "-", y, ":", minimum)

    total += minimum
    visited[y] = True

print("Minimum Cost =", total)