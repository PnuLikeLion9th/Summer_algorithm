# 프로그래머스_하샤드 수_수학_레벨 1
# 정수를 str()로 감싸주어서 각 자리수의 합을 더해주는 알고리즘 기법을 알면 쉽게 풀수 있는문제

def solution(x):
    num_sum = 0
    for num in str(x):  # 각 자리수를 더해주는 반복문
        num_sum += int(num)

    if x % num_sum == 0:  # x % 각 자리수의 합
        return True
    else:
        return False


# print(solution(int(input())))
