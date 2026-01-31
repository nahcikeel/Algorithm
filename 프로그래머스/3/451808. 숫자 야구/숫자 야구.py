def solution(n, submit):
    
    candidates = []
    for i in range(1000,10000):
        s = str(i)
        if '0' in s:
           continue
        if len(set(s)) == 4:
            candidates.append(s)

    def score(a,b):
        strike = sum(a[i] == b[i] for i in range(4))
        ball = sum((a[i] != b[i]) and (a[i] in b) for i in range(4))
        return strike, ball
               
    
    while len(candidates) > 1:
        guess = candidates[0]
        res = submit(int(guess))
        x = int(res[0])
        y = int(res[3])
               
        new_candidates = []
        for c in candidates:
            if score(guess,c) == (x,y):
                new_candidates.append(c)
        candidates = new_candidates
               
    return int(candidates[0])