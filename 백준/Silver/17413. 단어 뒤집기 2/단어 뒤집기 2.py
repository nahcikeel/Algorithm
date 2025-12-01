s = input().rstrip()

result = []
word = []
inside_tag = False

for ch in s:
    if ch == '<':
        result.extend(word[::-1])
        word = []
        inside_tag = True
        result.append(ch)

    elif ch == '>':
        inside_tag = False
        result.append(ch)

    elif inside_tag:
        result.append(ch)

    else:
        if ch == ' ':
            result.extend(word[::-1])
            result.append(' ')
            word = []
        else:
            word.append(ch)

result.extend(word[::-1])

print("".join(result))
