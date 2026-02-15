def solution(picks, minerals):
    answer = 0
    
    max_mine = sum(picks)*5
    minerals = minerals[:max_mine]
    
    groups = [minerals[i:i+5] for i in range(0,len(minerals),5)]
    score = []
    for group in groups:
        dia = group.count('diamond')
        iron = group.count('iron')
        stone = group.count('stone')
        total = (dia*25 + iron*5 + stone)
        score.append((total, dia, iron, stone))
        
    score.sort(reverse=True)
    for _, dia, iron, stone in score:
        if picks[0] > 0:
            picks[0] -= 1
            answer += (dia+iron+stone)
        elif picks[1] > 0:
            picks[1] -= 1
            answer += (dia*5+iron+stone)
        else:
            picks[2] -= 1
            answer += (dia*25+iron*5+stone)
    
    return answer