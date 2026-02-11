def solution(players, callings):
    
    pos = {player:idx for idx,player in enumerate(players)}
    
    for name in callings:
        ranking = pos[name]
        front = players[ranking-1]
        
        players[ranking-1],players[ranking]  = players[ranking], players[ranking-1]
        
        pos[front] += 1
        pos[name] -= 1 
        
        
    return players