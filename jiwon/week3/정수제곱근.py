def solution(n):
    sqrt = n ** (1/2) # 제곱근 구해서
    if sqrt % 1 == 0: # 나머지 연산했을 때 1로 나누어떨어지면 소수가 없는 것
        return (sqrt + 1) ** 2
    else:
        return -1