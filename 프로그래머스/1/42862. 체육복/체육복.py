def solution(n, lost, reserve):
    # 각 학생이 체육복을 가지고 있는 상태를 표시하는 리스트
    st = [1] * n
    
    # 체육복을 도난당한 학생들에 대해 상태를 업데이트
    for i in lost:
        st[i - 1] -= 1
    
    # 여분의 체육복을 가진 학생들에 대해 상태를 업데이트
    for i in reserve:
        st[i - 1] += 1
    
    # 체육복을 빌려주는 과정
    for i in range(n):
        if st[i] == 0:
            if i > 0 and st[i - 1] > 1:
                st[i] += 1
                st[i - 1] -= 1
            elif i < n - 1 and st[i + 1] > 1:
                st[i] += 1
                st[i + 1] -= 1
    
    # 체육 수업을 들을 수 있는 학생 수 계산
    answer = sum(1 for x in st if x > 0)
    
    return answer

# 예제 실행
print(solution(5, [2, 4], [3]))  # 예시: 5명의 학생 중 2번과 4번 학생이 잃어버렸고, 3번 학생이 여분을 가지고 있는 경우
