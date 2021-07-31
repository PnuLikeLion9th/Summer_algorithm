def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):#중간에 일치하지않으면
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(completion)]#끝까지 안걸리면