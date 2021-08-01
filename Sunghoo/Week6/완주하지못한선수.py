# 무조건 해시로 조져야하는 문제
# def solution(participant, completion):
#     answer = ''
#     parti = dict()
#     comple = dict()
#
#     for name in participant:
#         parti[name] = parti.get(name, 0) + 1
#         # try:
#         #     parti[name] += 1
#         # except KeyError:
#         #     parti[name] = 1
#
#     for name in completion:
#         comple[name] = comple.get(name, 0) + 1
#
#     for name in parti.keys():
#         if (parti[name] > 1 and parti[name] != comple[name]) or name not in comple:
#             answer = name
#             break
#     return answer


# get() 시간 복잡도가 시원찮네 => 효율성만 실패 => get() 이 문제가 아님 ㅎㅎ,, 위에 풀이 get()으로 고쳐도 ㄱ => get() dl try/except pattern 대신 사용하면 좋을
def solution(participant, completion):
    comple = dict()
    for name in completion:
        comple[name] = comple.get(name, 0) + 1
    for name in participant:
        if name not in comple:
            return name

        if participant.count(name) != comple[name]:
            return name


def solution(participant, completion):
    # 아니 최대 N 10만따리를 sort() 치는데도, 시간효율성 안터지네; O(NlogN)이라 그런가봄
    participant.sort()
    completion.sort()
    for parti, compl in zip(participant, completion):
        if parti != compl:
            return parti


import collections


def solution(participant, completion):
    return list(collections.Counter(participant) - collections.Counter(completion))[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
# participant =["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))
# 무조건 한명은 완주를 못했다는 명제를 잘 활용해야함
