n, new_score, p = map(int, input().split())

if n == 0:
    print(1)
else:
    scores = list(map(int, input().split()))

    if n == p and new_score <= scores[-1]:
        print(-1)
    else:
        rank = 1
        for s in scores:
            if s > new_score:
                rank += 1
            else:
                break
        print(rank)
