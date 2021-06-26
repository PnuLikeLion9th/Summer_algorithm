def solution(phone_number):
    #문자열에 정수를 곱하면 문자열이 반복된다.
    return '*' * (len(phone_number) -4) + phone_number[-4:]
    



print(solution("01033334444"))