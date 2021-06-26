def solution(x, n):
    answer = []
    index = 0
    for i in range(n):
        index = index + x
        answer.append(index)
    return answer