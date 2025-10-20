n = int(input())

start = 1
end = 1
cur_sum = 1
cnt = 0

while start<=n:
    if cur_sum == n:
        cnt += 1
        end += 1
        cur_sum += end
    elif cur_sum < n:
        end += 1
        cur_sum += end
    else:
        cur_sum -= start
        start += 1
print(cnt)