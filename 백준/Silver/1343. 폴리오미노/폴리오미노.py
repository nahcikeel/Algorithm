board = input()

parts = board.split('.')
result = []

for part in parts:
    length = len(part)
    
    if length % 2 == 1:
        print(-1)
        exit()

    result.append("AAAA" * (length // 4) + "BB" * ((length % 4) // 2))

print('.'.join(result))
