def solution(N, stages):

    challenger = len(stages)
    n_stage = dict()
    
    for i in range(1,N+1):
        if challenger != 0:
            fail_num = stages.count(i)
            n_stage[i] = fail_num / challenger
            challenger -= fail_num
        else:
            n_stage[i] = 0
            
    answer = sorted(n_stage, key=lambda x:n_stage[x], reverse=True)
            
    return answer