def solution(phone_number):
    
    front_num = '*' * (len(phone_number)-4)
    back_num = phone_number[-4:]
    
    answer = front_num + back_num
    
    return answer 