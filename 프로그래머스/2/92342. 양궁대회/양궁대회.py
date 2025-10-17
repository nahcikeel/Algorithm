MAX_DIFF = 0
BEST_RYAN_SHOT = [-1]

def solution(n, info):
    global MAX_DIFF, BEST_RYAN_SHOT
    idx = 0
    ryan_shot = [0]*11
    dfs(n, idx, ryan_shot, info)

    return BEST_RYAN_SHOT

def dfs(n_left, idx, ryan_shot, apeach_info):
    global MAX_DIFF, BEST_RYAN_SHOT
    
    if idx == 11:
        if n_left > 0 :
            ryan_shot[10] = n_left
        
        calculate_score(ryan_shot, apeach_info)
        if n_left > 0:
            ryan_shot[10] = 0
        return
    
    required_arrows = apeach_info[idx] + 1
    if n_left >= required_arrows:
        ryan_shot[idx] = required_arrows
        dfs(n_left - required_arrows, idx+1, ryan_shot, apeach_info)
    ryan_shot[idx] = 0
    dfs(n_left, idx+1, ryan_shot, apeach_info)
    
    
def calculate_score(ryan_shot, apeach_info):
    global MAX_DIFF, BEST_RYAN_SHOT
    
    ryan_score, apeach_score = 0, 0
    
    for i in range(11):
        score = 10-i
        if ryan_shot[i]==0 and apeach_info[i]==0:
            continue
            
        if ryan_shot[i] > apeach_info[i]:
            ryan_score += score
        else:
            apeach_score += score
    
    diff = ryan_score - apeach_score
    if diff > 0:
        if diff > MAX_DIFF:
            MAX_DIFF = diff
            BEST_RYAN_SHOT = list(ryan_shot)
        elif diff == MAX_DIFF:
            if is_better(ryan_shot, BEST_RYAN_SHOT):
                BEST_RYAN_SHOT = list(ryan_shot)

def is_better(new_shot, old_shot):
    for i in range(10,-1,-1):
        if new_shot[i] > old_shot[i]:
            return True
        elif new_shot[i] < old_shot[i]:
            return False
    return False
    
    
            