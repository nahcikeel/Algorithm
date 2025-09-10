from collections import Counter

def make_pair(s):
    s = s.lower()
    pairs = []
    for i in range(len(s)-1):
        pair = s[i:i+2]
        if pair.isalpha():
            pairs.append(pair)
    return Counter(pairs)

def solution(str1, str2):
    c1 = make_pair(str1)
    c2 = make_pair(str2)
    
    inter = c1 & c2
    union = c1 | c2
    
    inter_size = sum(inter.values())
    union_size = sum(union.values())
    
    if union_size == 0:
        return 65536
    
    return int(inter_size/union_size * 65536)
    
    return inter