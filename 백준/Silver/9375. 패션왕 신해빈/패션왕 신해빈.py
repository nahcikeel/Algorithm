T = int(input())

for _ in range(T):
    clothes = {}
    n = int(input())

    for i in range(n):
        acc, category = input().split()

        if category not in clothes: 
            clothes[category] = [acc]
        else:
            new_cloth = clothes.get(category)
            new_cloth.append(acc)
            clothes[category] = new_cloth
    
    cnt = 1
    for cloth in clothes:
        cnt *= len(clothes[cloth]) + 1
    print(cnt - 1)