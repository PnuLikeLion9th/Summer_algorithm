# 투 포인터 이용
def solution(people, limit):
    people.sort()
    lp, rp = 0, len(people) - 1  # i는 처음 원소의 인덱스, j는 마지막 원소의 인덱스를 가리킴
    answer = 0
    while lp <= rp:
        answer += 1
        if people[lp] + people[rp] <= limit:
            lp += 1
        rp -= 1
    return answer
