def solution(n):
    s = set(i for i in range(2, n+1))
    for i in range(2, n+1):
        s -= set(j for j in range(2*i, n+1, i))
    return len(s)