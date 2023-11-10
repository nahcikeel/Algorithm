Self = list(range(1,10001))
notSelf = []
a = 0

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    if i <= 10000:
            notSelf.append(i)

notSelf = list(set(notSelf))

for m in notSelf:
    if m in Self:
        Self.remove(m)

for n in Self:
    print(n)