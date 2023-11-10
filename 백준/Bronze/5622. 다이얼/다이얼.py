dials = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
number = 0
n = input()

for i in n:
    for dial in dials:
        if i in dial:
            number += (dials.index(dial)+3)
print(number)