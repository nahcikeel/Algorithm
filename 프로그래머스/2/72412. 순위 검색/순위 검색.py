from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = {}

    for line in info:
        data = line.split()
        conditions = data[:-1]
        score = int(data[-1])

        for i in range(5):
            for comb in combinations(range(4), i):
                temp = conditions[:]
                for idx in comb:
                    temp[idx] = '-'
                key = ''.join(temp)
                if key in dic:
                    dic[key].append(score)
                else:
                    dic[key] = [score]
                # dic.setdefault(key, []).append(score)

    for key in dic:
        dic[key].sort()

    for q in query:
        q = q.replace(' and ', ' ')
        q = q.split()

        key = ''.join(q[:-1])
        target_score = int(q[-1])

        if key in dic:
            scores = dic[key]
            idx = bisect_left(scores, target_score)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)

    return answer
