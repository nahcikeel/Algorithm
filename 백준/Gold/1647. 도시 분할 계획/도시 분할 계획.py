import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(m):
    a,b,c = map(int, input().split())
    graph.append((c,a,b))

graph.sort()

parent = [i for i in range(n+1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a_root = find(a)
    b_root = find(b)

    if a_root == b_root:
        return False
    parent[b_root] = a_root
    return True

mst_cost = 0
max_graph = 0

for c, a, b in graph:
    if union(a,b):
        mst_cost += c
        max_graph = max(max_graph, c)

print(mst_cost - max_graph)