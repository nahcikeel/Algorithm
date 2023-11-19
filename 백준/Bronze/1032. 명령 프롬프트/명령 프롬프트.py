n = int(input())
pat1 = list(input())

for i in range(n-1):
    pat2 = input()

    for i in range(len(pat1)):
        if pat1[i] != pat2[i]:
            pat1[i] = '?'


print(''.join(pat1))