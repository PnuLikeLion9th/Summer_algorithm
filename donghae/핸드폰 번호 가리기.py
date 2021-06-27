def solution(phone_number):
    #문자열 슬라이싱에서 끝 번호는 포함되지 않음
    answer = len(phone_number[0:-4])*'*' + phone_number[-4:]
    return answer