# 내장함수 math.gcd, math.lcm도 있음
# 여기서 gcd는 유클리드 호제법으로 구함.

def solution(n, m):
    return [gcd(n, m), n*m/gcd(n, m)]  # [최대공약수, 최소공배수] 반환


def gcd(a, b):  # 유클리드 호제법
    while(b):
        a, b = b, a % b
    return a
