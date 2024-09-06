def solution(record):
    answer = []
    chat = {}
    
    for rec in record:
        temp = rec.split()
        
        com = temp[0]
        user = temp[1]
        
        if com == 'Enter' or com == 'Change':
            chat[user] = temp[2]
    
    for rec2 in record:
        result = rec2.split()
        
        command = result[0]
        user = result[1]
        
        if command == 'Enter':
            name = chat[user]
            answer.append(''.join([name,'님이 들어왔습니다.']))
            
        elif command == 'Leave':
            name = chat[user]
            answer.append(''.join([name,'님이 나갔습니다.']))
        
        
        
        
    
    return answer