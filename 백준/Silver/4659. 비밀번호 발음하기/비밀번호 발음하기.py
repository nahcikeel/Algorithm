moum = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input()
    if password == 'end':
        break

    has_moum = False
    m_cnt = 0
    j_cnt = 0
    prev = ''
    acceptable = True
    
    for p in password:
        if p in moum:
            has_moum = True
            m_cnt += 1
            j_cnt = 0
        else:
            j_cnt += 1
            m_cnt = 0

        if m_cnt == 3 or j_cnt == 3:
            acceptable = False
            break
        
        if prev == p and p != 'e' and p != 'o':
            acceptable = False
            break
        
        prev = p
    
    if not has_moum:
        acceptable = False
    
    if acceptable:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')