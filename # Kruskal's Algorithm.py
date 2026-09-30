# Kruskal's Algorithm

n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

edges = []

print("Enter edges: source destination weight")

for i in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = []

for i in range(n):
    parent.append(i)

total = 0
count = 0

print("\nEdges in MST:")

for w, u, v in edges:

    a = u
    while parent[a] != a:
        a = parent[a]

    b = v
    while parent[b] != b:
        b = parent[b]

    if a != b:

        print(u, "-", v, ":", w)

        total += w
        count += 1

        parent[b] = a

        if count == n - 1:
            break

print("Minimum Cost =", total)