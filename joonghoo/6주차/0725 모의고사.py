# 프로그래머스_모의고사_브루트포스_레벨 1
# 1,2,3 번 수포자가 푸는 방식을 list에 저장한뒤 입력된 정답과 비교하면서 맞은 개수를 count 하면 된다
# 이때 정답의 길이가 최대 1만이므로 list의 길이를 10000으로 설정한다

def solution(answers):
    numbers1 = [1, 2, 3, 4, 5]*2000  # 1번 수포자가 찍는 방식
    numbers2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250  # 2번 수포자가 찍는 방식
    numbers3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000  # 3번 수포자가 찍는 방식
    count_1, count_2, count_3 = 0, 0, 0
    for i in range(len(answers)):  # 입력된 정답과 같을 경우 count++
        if answers[i] == numbers1[i]:
            count_1 += 1
        if answers[i] == numbers2[i]:
            count_2 += 1
        if answers[i] == numbers3[i]:
            count_3 += 1

    result = []
    max_count = max(count_1, count_2, count_3)
    # 높은 점수를 받은 사람을 판별하여 result에 저장
    if max_count == count_1:
        result.append(1)
    if max_count == count_2:
        result.append(2)
    if max_count == count_3:
        result.append(3)

    return result
