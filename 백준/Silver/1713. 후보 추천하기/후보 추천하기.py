N = int(input())
R = int(input())
recs = list(map(int, input().split()))

frame = dict()
time = 0

for r in recs:
    if r in frame:
        frame[r][0] += 1
    else:
        if len(frame) >= N:
            min_rec = min(frame.values(), key=lambda x: (x[0], x[1]))[0]
            to_remove = min(frame.items(), key=lambda x: (x[1][0], x[1][1]))[0]
            del frame[to_remove]
        frame[r] = [1, time]
    time += 1

result = sorted(frame.keys())
print(*result)
