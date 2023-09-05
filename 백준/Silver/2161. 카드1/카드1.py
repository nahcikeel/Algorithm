n = int(input())

ki = []
chan = []

for i in range(1,n+1):
    ki.append(i)

while len(ki) > 0:
    chan.append(ki.pop(0))
    if len(ki) > 0:
        ki.append(ki.pop(0))

for j in chan:
    print(j, end=" ")