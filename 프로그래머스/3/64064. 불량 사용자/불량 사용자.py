from itertools import product

def solution(user_id, banned_id):
    result = []
    
    for ban in banned_id:
        n = len(ban)
        match = []
        
        for user in user_id:
            if len(user) == n:
                for i in range(n):
                    if user[i] != ban[i] and ban[i] != '*':
                        break
                else:
                    match.append(user)
                    
        result.append(match)
        
    product_list = list(product(*result))
    unique_set = set()

    for pro in product_list:
        if len(set(pro)) == len(pro):
            unique_set.add(frozenset(pro))
    
    return len(unique_set)