# 통과
def solution(participant, completion):
    answer = ''
    parti = dict()
    comple = dict()

    for name in participant:
        try:
            parti[name] += 1
        except KeyError:
            parti[name] = 1

    for name in completion:
        try:
            comple[name] += 1
        except KeyError:
            comple[name] = 1

    for name in parti:
        print(name)
        if parti[name] > 1:
            if parti[name] == comple[name]:
                pass
            else:
                answer = name
                break
        elif name not in comple:
            answer = name
            break
    return answer


# 케이스 통과/ 효율성 실패
def solution(participant, completion):
    comple = dict()

    for name in completion:
        try:
            comple[name] += 1
        except KeyError:
            comple[name] = 1

    for name in participant:
        if name not in comple:
            return name

        if participant.count(name) != comple[name]:
            return name


# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
# print(solution(participant, completion))


# participant 가 10만이므로, 그대로 for 문 돌리는 것은 시간초과 가능성 있다.
# 10만 participant 중 중복되는 원소도 존재하기 때문에, 이 중복을 제거하여 연산할 수 있는 Hash 를 사용해야 시간효율성을 극복할 수 있다.
