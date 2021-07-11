def solution(n):
    point = 0
    i = 1
    while i * i <= n:
        if i * i == n:
            return (i+1) * (i+1)
        i = i + 1

    return -1


print(solution(121))
