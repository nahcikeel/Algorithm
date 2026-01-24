n, game = input().split()
n = int(n)

players = set()
for _ in range(n):
    players.add(input().strip())

if game == 'Y':
    print(len(players))
elif game == 'F':
    print(len(players) // 2)
else:  # 'O'
    print(len(players) // 3)
