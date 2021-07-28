def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if not p == c:
            return p
    return participant[-1]
