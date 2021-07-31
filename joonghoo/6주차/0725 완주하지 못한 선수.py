# 프로그래머스_완주하지 못한 선수_해시_레벨 1
# 두 list를 정렬하고 하나씩 비교한다.
# 다른값이 존재할경우 그 값을 return
# for문이 종료 될때까지 다른값이 없을경우 마지막값을 return


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:  # 다른값이 나올 경우
            return participant[i]  # 다른 값 return
    return participant[-1]  # 마지막 값만 다른 경우는 마지막값 return


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
