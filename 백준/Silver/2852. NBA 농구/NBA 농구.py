def to_sec(t):
    m, s = map(int, t.split(':'))
    return m * 60 + s


def to_mmss(s):
    return f"{s//60:02d}:{s%60:02d}"

n = int(input())

score1 = 0
score2 = 0

time1 = 0
time2 = 0

prev_time = 0

for _ in range(n):
    team, time = input().split()
    cur_time = to_sec(time)

    if score1 > score2:
        time1 += cur_time - prev_time
    elif score2 > score1:
        time2 += cur_time - prev_time

    if team == '1':
        score1 += 1
    else:
        score2 += 1

    prev_time = cur_time

end_time = 48*60
if score1 > score2:
    time1 += end_time - prev_time
elif score2 > score1:
    time2 += end_time - prev_time

print(to_mmss(time1))
print(to_mmss(time2))