import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

def binary_func(a,b):                        # 이진분류를 실행할 함수 생성

    start = 0                                # 처음 숫자
    end = len(a)-1                           # 마지막 숫자

    while start <= end:                     # 처음과 마지막을 좁혀오는 동안 반복
        mid = (start+end) // 2              # 중간 지점 
        
        if b == a[mid]:                     # a의 원소가 b와 같다면?
            return 1                        # 1 반환
        
        elif b > a[mid]:                    # b의 원소가 중간 이후에 있다면 오른쪽 탐색(오른쪽으로 기준 +1)
            start = mid +1                  
        
        else:                               # b의 원소가 중간 이전에 있다면 왼쪽 탐색(왼쪽으로 기준 +1)
            end = mid -1                
            
    return 0

for i in range(m):
    print(binary_func(a,b[i]))              # a와 비교할 b의 원소를 전달
