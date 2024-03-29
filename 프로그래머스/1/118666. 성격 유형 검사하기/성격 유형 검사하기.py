def solution(survey, choices):
    checker = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    answer = []

    for i in range(len(choices)):
        if choices[i]>4:
            checker[survey[i][1]] += score[choices[i]]

        elif choices[i]<4:
            checker[survey[i][0]] += score[choices[i]]

    if checker['R'] > checker['T']:
        answer.append('R')
    elif checker['R'] == checker['T']:
        answer.append('R')
    else:
        answer.append('T')

    if checker['C'] > checker['F']:
        answer.append('C')
    elif checker['C'] == checker['F']:
        answer.append('C')
    else:
        answer.append('F')

    if checker['J'] > checker['M']:
        answer.append('J')
    elif checker['J'] == checker['M']:
        answer.append('J')
    else:
        answer.append('M')

    if checker['A'] > checker['N']:
        answer.append('A')
    elif checker['A'] == checker['N']:
        answer.append('A')
    else:
        answer.append('N')

    answer = ''.join(answer)
    return answer