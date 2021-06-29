def solution(num):
    n = 0
    while num != 1: #num이 1이 될 때 까지
        n += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        if n > 500:     #횟수가 500을 넘으면 -1반환
            return -1
    return n