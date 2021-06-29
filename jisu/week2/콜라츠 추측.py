def solution(num):
    answer = 0
    while(num != 1):  # 주어진 수가 1이 아닐 때까지 반복
        if answer == 500:  # 작업을 반복한 횟수가 500이면 -1 반환
            return -1
        num = num*3+1 if num % 2 else num/2  # 작업순서
        answer += 1  # 작업 횟수 증가
    return answer
