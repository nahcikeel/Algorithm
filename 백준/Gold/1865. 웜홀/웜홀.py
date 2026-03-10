import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    n, m, w = map(int, input().split())

    edges = []

    for _ in range(m):
        s,e,t = map(int,input().split())
        edges.append((s,e,t))
        edges.append((e,s,t))

    for _ in range(w):
        s,e,t = map(int,input().split())
        edges.append((s,e,-t))

    dist = [0]*(n+1)

    cycle = False

    for i in range(n):
        for s,e,t in edges:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n-1:
                    cycle = True

    print("YES" if cycle else "NO")