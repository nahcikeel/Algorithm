n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

left = 0
right = (n-1)

result = float('inf')
ans = [0,0]

while left<right:
    diff = abs(liquids[left] + liquids[right])

    if diff < result:
        ans = [liquids[left], liquids[right]]
        result = diff

    if liquids[left] + liquids[right] < 0:
        left += 1
    else:
        right -= 1
        
print(ans[0], ans[1])