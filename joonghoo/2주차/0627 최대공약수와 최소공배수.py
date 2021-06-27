# 프로그래머스_최대공약수와 최소공배수_수학_레벨 1
# 유클리드 호제법으로 최대공약수를 구하고, a*b/gcd 하면 최소공배수가 나온다.

def solution(n, m):
    answer = []
    answer.append(gcd(n, m))  # 최대공약수 append
    answer.append(n*m//answer[0])  # 최대공약수 append
    return answer


def gcd(n, m):  # 유클리드 호제법으로 최대공약수를 구함
    a = max(n, m)
    b = min(n, m)
    while b:
        num = a % b
        a = b
        b = num
    return a


# n, m = map(int, input().split())
# print(solution(n, m))
