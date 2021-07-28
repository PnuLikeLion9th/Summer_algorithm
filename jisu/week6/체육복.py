def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost:  # 체육복 안 잃어버림
            answer += 1
        else:  # 잃어버렸지만, 여분 있음
            if i in reserve:
                answer += 1
                reserve.remove(i)
                lost.remove(i)
    for i in lost:  # 잃어버렸고, 여분도 없어서 빌려야 함
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)

    return answer
