# 프로그래머스_약수의 개수와 덧셈_수학_레벨 1

def solution(left, right):
    sum = 0
    for i in range(left, right+1):  # left ~ right 까지 반복문 진행
        count = 0  # 약수의 개수를 나타낼 변수 count 초기화
        for j in range(1, i+1):
            if i % j == 0:  # i의 약수의 갯수를 count
                count += 1
        if count % 2 == 0:  # 약수의 개수가 짝수면 +
            sum += i
        else:  # 홀수면 -
            sum -= i
    return sum
