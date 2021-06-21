# 프로그래머스_x만큼 간격이 있는 n개의 숫자_수학_레벨 1

def solution(x, n):
    answer = []
    sum = x  # x를 계속 활용해야 하므로 sum에 x 값 저장
    for _ in range(n):  # n번만큼 반복
        answer.append(sum)  # 변화하는 sum의 값을 answer 리스트에 저장
        sum += x  # sum에 x만큼 더해준다
    return answer


print(solution(2, 5))
