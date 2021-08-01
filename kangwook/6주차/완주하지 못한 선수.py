def solution(participant,completion):
    # for i in completion:
    #     participant.remove(i)
    # return participant[0]

    # if len(participant) == len(set(participant)): 
    #     return (set(participant)-set(completion)).pop()
    # else:
    #     if set(participant) != set(completion):
    #         return (set(participant)-set(completion)).pop()
    #     else:
    #         for i in participant:
    #             if participant.count(i) >=2:
    #                 return i

    if len(set(participant)-set(completion)) != 0: 
        return set(participant)-set(completion).pop()
    elif len(set(participant)-set(completion)) == 0:
        for i in completion:
            participant.remove(i)
        return participant[0]