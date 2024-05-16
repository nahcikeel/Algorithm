import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))  #집 개수 N, 공유기 C개

houses = [int(input().rstrip()) for _ in range(n)]

houses.sort()

start = 1
end = houses[-1] - houses[0]
answer = 0

while (start<=end):
    mid = (start + end) // 2
    cnt = 1
    machine = houses[0]

    for i in range(1,n):
        if houses[i] - machine >= mid:
            cnt += 1
            machine = houses[i]
    if cnt >= c:
        answer = mid
        start = mid + 1

    else:
        end = mid-1

print(answer)