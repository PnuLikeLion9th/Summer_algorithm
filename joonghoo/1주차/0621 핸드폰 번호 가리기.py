# 프로그래머스_핸드폰 번호 가리기_문자열_레벨 1
# 문자열 슬라이싱을 사용하는 문제
# 변수 phone_number가 정해지지 않았기 때문에 phone_number 길이 -4 만큼 별로 바꿔주고, 끝에 4는 그대로 출력한다.

def solution(phone_number):
    return (len(phone_number)-4) * '*' + phone_number[-4:]


phone_number = "01033334444"
print(solution(phone_number))
