import math

def solution(n):
    x = int(math.sqrt(n))   #제곱근 계산 후 int형으로 변환
    if x ** 2 != n: #x의 제곱이 n이 아닌 경우 -1반환
        return -1
    return (x + 1) ** 2