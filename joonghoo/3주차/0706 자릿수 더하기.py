# 프로그래머스_자릿수 더하기_수학_레벨 1
# 길이가 2 이상인 숫자에 문자형태로 변환하게 될 경우 각각의 자릿수로 나누어 진다는것을 이용한다
# ex) str(123) ==> '1', '2', '3'

def solution(n):
    sum = 0
    for num in str(n):  # n을 str형태로 변환한뒤, 각각의 자릿수인 num을 더해준다
        sum += int(num)
    return sum
