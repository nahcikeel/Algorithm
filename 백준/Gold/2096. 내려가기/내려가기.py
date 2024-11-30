n = int(input())

prev_max = list(map(int, input().split()))
prev_min = prev_max[:]

for _ in range(1,n):
    current = list(map(int, input().split()))

    new_max = [
                current[0] + max(prev_max[0],prev_max[1]),
                current[1] + max(prev_max[0],prev_max[1], prev_max[2]),
                current[2] + max(prev_max[1],prev_max[2])
    ]

    new_min = [
                current[0] + min(prev_min[0],prev_min[1]),
                current[1] + min(prev_min[0],prev_min[1], prev_min[2]),
                current[2] + min(prev_min[1],prev_min[2])
    ]

    prev_max = new_max
    prev_min = new_min
       
print(max(prev_max), min(prev_min))