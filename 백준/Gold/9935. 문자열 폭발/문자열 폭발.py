word = input()
bomb = input()

n = len(bomb)
stack = []

for w in word:
    stack.append(w)
    if ''.join(stack[-n:]) == bomb:
        del stack[-n:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')