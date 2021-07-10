# 프로그래머스_약수의 합_수학_레벨 1
# 1부터 n까지의 반복문에서 n을 i로 나눴을때 나머지가 0이면 i는 n의 약수이다.

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:  # n의 약수 i를 구하는 조건문
            answer += i  # 약수를 더해준다

    return answer
