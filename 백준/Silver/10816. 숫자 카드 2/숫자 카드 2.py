import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

chan = {}

for i in a:              
    if i in chan:       # a의 원소가 chan에 있다면, a:n (1씩 증가)
        chan[i] += 1    
    else:               # a의 원소가 chan에 없다면 a:1
        chan[i] = 1

for j in b:             
    if j in chan:       # b의 원소가 chan에 있다면 a:n => n 출력
        print(chan[j])  
    else:               # b의 원소가 chan에 없다면 a:0 => 0 출력
        print(0)