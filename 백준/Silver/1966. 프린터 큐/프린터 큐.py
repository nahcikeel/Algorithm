from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))

    cnt = 0
    index = [i for i in range(n)]

    while q:
        if q[0] == max(q):
            
            cnt += 1

            if index[0] == m:
                print(cnt)
                break

            else:
                q.popleft()
                del index[0]

        elif q[0] < max(q):
            q.append(q.popleft())
            index.append(index[0])
            del index[0]