T = int(input())

for _ in range(T):
    data = list(map(int, input().split()))
    test_id = data[0]
    heights = data[1:]

    moves = 0
    for i in range(20):
        for j in range(i):
            if heights[j] > heights[i]:
                moves += 1

    print(test_id, moves)
