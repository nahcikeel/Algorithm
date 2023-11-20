n = int(input())
rope = []
w = []

for _ in range(n):
    rope.append(int(input()))
    
rope.sort(reverse=True)

for i in range(n):
    w.append(rope[i]*(i+1))

print(max(w))