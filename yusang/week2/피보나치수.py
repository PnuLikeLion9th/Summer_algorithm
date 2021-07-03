def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(1, n):
        answer = a + b
        a = b
        b = answer

    return answer % 1234567

print(solution(3))