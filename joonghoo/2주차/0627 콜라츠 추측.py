# 프로그래머스_콜라츠 추측_수학_레벨 1

def solution(num):
    count = 0
    while num != 1:  # num이 1이 될때까지 반복
        count += 1  # 반복횟수 체크
        if count == 500:  # 500번 반복하면 반복문 종료
            count = -1
            break
        if num % 2 == 0:  # num이 짝수일때
            num /= 2
        else:  # num 이 홀수일떄
            num *= 3
            num += 1
    return count


# n = int(input())
# print(solution(n))
