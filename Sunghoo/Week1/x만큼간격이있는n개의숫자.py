def solution(x, n):
    # answer = []
    # if x == 0:
    #     return [0]*n
    return [i if x != 0 else [0] * n for i in range(x, x*(n+1), x)]
