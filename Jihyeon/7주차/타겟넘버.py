def solution(numbers, target):
    answer = 0
    leaves = [0]
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp                            # leaves리스트에 모든 계산 결과 담기
    for leaf in leaves:                         # target값과 비교해서 결과 출력
        if leaf == target:
            answer += 1
    return answer