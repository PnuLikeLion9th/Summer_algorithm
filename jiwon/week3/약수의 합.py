def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0: #나눠서 나머지없는 약수들 구해주고
            answer += i #모두더하기
    return answer