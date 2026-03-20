from collections import defaultdict

def dfs(sell, price, graph, ref_dict):
    if sell == '-' or price < 1:
        return
    give = int(price * 0.1)
    graph[sell] += price - give
    dfs(ref_dict[sell], give, graph, ref_dict)

    
def solution(enroll, referral, seller, amount):
    
    # 다단계 그래프 생성
    ref_dict = {enroll[i] : referral[i] for i in range(len(enroll))}
    amount = [i*100 for i in amount]
    
    # 점수 계산용
    graph = defaultdict(int)
    for e in enroll:
        graph[e] = 0
    
    # 점수 계산
    for i in range(len(seller)):
        dfs(seller[i], amount[i], graph, ref_dict)
    
    # 처리
    answer = []
    for _,i in graph.items():
        answer.append(i)
    
    return answer