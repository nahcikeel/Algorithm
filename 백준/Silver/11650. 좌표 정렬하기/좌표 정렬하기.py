n = int(input())
stars = []

for _ in range(n):
    x,y = input().split()
    stars.append([int(x),int(y)])

stars.sort()

for star in stars:
    print(star[0],star[1])