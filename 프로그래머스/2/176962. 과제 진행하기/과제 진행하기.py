def to_min(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
def solution(plans):
    answer = []

    plans = [(name, to_min(start), int(play)) for name, start, play in plans]
    plans.sort(key=lambda x: x[1])

    stack = []

    for i in range(len(plans)):
        name, start, play = plans[i]
        
        if i < len(plans) - 1:
            next_start = plans[i + 1][1]
            available = next_start - start
        else:
            available = float('inf')  # 마지막 과제

        if play <= available:
            answer.append(name)
            available -= play

            # 남은 시간 동안 스택 과제 처리
            while stack and available > 0:
                prev_name, prev_play = stack.pop()
                if prev_play <= available:
                    answer.append(prev_name)
                    available -= prev_play
                else:
                    stack.append((prev_name, prev_play - available))
                    break
        else:
            stack.append((name, play - available))
            continue

    while stack:
        answer.append(stack.pop()[0])

    return answer
