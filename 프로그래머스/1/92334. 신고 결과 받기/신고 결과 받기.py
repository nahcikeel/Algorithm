def solution(id_list, report, k):
    answer = []
    
    report_set = set(report)
    people = {user_id:set() for user_id in id_list}
    
    for rep in report:
        reporter, reportee = rep.split()
        people[reportee].add(reporter)
    
    stop_users = set()
    for reportee, reporter in people.items():
        if len(reporter) >= k:
            stop_users.add(reportee)
            
    mails = {user_id:0 for user_id in id_list}
    for user in stop_users:
        reporters = people[user]
        for r in reporters:
            mails[r] += 1
    
    result = []
    for user_name, cnt in mails.items():
        result.append(cnt)
    
    return result