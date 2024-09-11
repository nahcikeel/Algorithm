from dateutil.relativedelta import relativedelta
from datetime import datetime

def solution(today, terms, privacies):
    
    answer = []
    term_dict = {}
    today = datetime.strptime(today, "%Y.%m.%d")
    
    # 약관 딕셔너리에 저장
    for term in terms:
        name, til = term.split()
        term_dict[name] = int(til)
    
    # 각 기간 비교
    for i in range(len(privacies)):
        date, name = privacies[i].split()
        
        cp_date = datetime.strptime(date, "%Y.%m.%d") + relativedelta(months = term_dict[name])
        if cp_date <= today:
            answer.append(i+1)
        
    return answer