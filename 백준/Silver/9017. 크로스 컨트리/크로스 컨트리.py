from collections import Counter

T = int(input())
for _ in range(T):

    n = int(input())
    scores = list(map(int, input().split()))



    count = Counter(scores)
    valid = set(team for team in count if count[team]>=6)  # 유효한 팀

    team_score = {team:0 for team in valid}
    team_cnt = {team:0 for team in valid}
    fifth = dict()

    rank = 1
    for s in scores:
        if s not in valid:
            continue
        team_cnt[s] += 1
        if team_cnt[s] <= 4:
            team_score[s] += rank
        elif team_cnt[s] == 5:
            fifth[s] = rank
        
        rank += 1

    answer = min(valid, key = lambda x: (team_score[x], fifth[x]))
    print(answer)