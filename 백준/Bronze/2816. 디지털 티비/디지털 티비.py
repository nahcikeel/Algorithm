n = int(input())
channels = [input().strip() for _ in range(n)]

res = []
cursor = 0

# 1. KBS1을 첫 번째로
idx = channels.index("KBS1")

# 커서 이동
while cursor < idx:
    res.append('1')
    cursor += 1
while cursor > idx:
    res.append('2')
    cursor -= 1

# 위로 끌어올리기
while cursor > 0:
    res.append('4')
    channels[cursor], channels[cursor - 1] = channels[cursor - 1], channels[cursor]
    cursor -= 1

# 2. KBS2를 두 번째로
idx = channels.index("KBS2")

while cursor < idx:
    res.append('1')
    cursor += 1
while cursor > idx:
    res.append('2')
    cursor -= 1

while cursor > 1:
    res.append('4')
    channels[cursor], channels[cursor - 1] = channels[cursor - 1], channels[cursor]
    cursor -= 1

print(''.join(res))
