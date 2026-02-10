def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        a = format(arr1[i], f'0{n}b')
        b = format(arr2[i], f'0{n}b')

        line = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)

    return answer
