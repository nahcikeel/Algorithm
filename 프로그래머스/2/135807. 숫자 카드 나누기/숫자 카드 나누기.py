from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)

    answer = 0

    # gcdA가 B를 하나도 나누지 못하면 후보
    if all(b % gcdA != 0 for b in arrayB):
        answer = gcdA

    # gcdB가 A를 하나도 나누지 못하면 후보
    if all(a % gcdB != 0 for a in arrayA):
        answer = max(answer, gcdB)

    return answer
