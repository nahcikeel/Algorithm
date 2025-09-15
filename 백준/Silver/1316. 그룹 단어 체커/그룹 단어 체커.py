n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    is_group = True
    seen = set()
    prev = ''
    for w in word:
        if w != prev:
            if w in seen:
                is_group = False
                break
            else:
                seen.add(w)
        prev = w
    if is_group:
        cnt += 1
print(cnt)