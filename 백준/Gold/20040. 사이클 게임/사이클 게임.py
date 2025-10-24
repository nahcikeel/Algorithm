import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n,m = map(int, input().split())

parent = [i for i in range(n)]

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

result = 0
for i in range(m):
    a,b = map(int , input().split())
    if not union(a,b):
        result = i+1
        break

print(result)