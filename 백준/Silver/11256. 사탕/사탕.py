for _ in range(int(input())):       # T
    j, n = map(int, input().split())    # J, N : 사탕 개수, 상자 개수
    box = []
    for i in range(n):
        r, c = map(int, input().split())    # N 상자의 각 가로,세로 사이즈
        box.append(r*c)      # N개 상자 크기
    box.sort(reverse=True)

    cnt = 0

    while j > 0:
        j -= box[cnt]
        cnt += 1
        
    print(cnt)