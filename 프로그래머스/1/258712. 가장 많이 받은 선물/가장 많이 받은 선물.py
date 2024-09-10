def solution(friends, gifts):
    answer = []
    n = len(friends)
    
    # 선물 지수
    score_dict = {}
    
    for friend in friends:
        score_dict[friend] = 0
    
    # 선물 테이블
    score = [[0 for _ in range(n)] for _ in range(n)]
    
    for gift in gifts:
        give, take = gift.split()
        
        score_dict[give] += 1
        score_dict[take] -= 1
        
        g_idx = friends.index(give)
        t_idx = friends.index(take)
        
        score[g_idx][t_idx] += 1
    
    # 계산 
    for i in range(n):
        cnt = 0
        for j in range(n):
            if i != j:
                
                if score[i][j] > score[j][i]:
                    cnt += 1
                    
                elif score[i][j] == score[j][i]:
                    if score_dict[friends[i]] > score_dict[friends[j]]:
                        cnt += 1

                    
        answer.append(cnt)
    
    return max(answer)