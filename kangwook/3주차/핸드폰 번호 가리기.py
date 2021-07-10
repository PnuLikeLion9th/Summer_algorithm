def solution(phone_number):
    answer='*'*(len(str(phone_number))-4)+phone_number[-4:]
    return answer