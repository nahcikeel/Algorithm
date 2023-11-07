cro_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

a = input()

for cro in cro_list:
    if cro in a:
        a = a.replace(cro,'1')

print(len(a))