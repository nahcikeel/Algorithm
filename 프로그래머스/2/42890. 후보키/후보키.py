from itertools import combinations

def solution(relation):
    
    rows = len(relation)
    cols = len(relation[0])
    candidates = []
    
    for size in range(1, cols+1):
        for comb in combinations(range(cols), size):
            
            # 유일성 체크
            tmp = set()
            for row in relation:
                tmp.add(tuple(row[c] for c in comb))
            if len(tmp) != rows:
                continue
            
            # 최소성 체크
            is_minimal = True
            for candidate in candidates:
                if set(candidate).issubset(set(comb)):
                    is_minimal = False
            if is_minimal:
                candidates.append(comb)
                
            
    
    return len(candidates)