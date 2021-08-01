def solution(record):
    idList = {}
    answer = []

    for act in record:
        if len(act.split()) < 3:
            idList[act.split()[1]] = act.split()[2]
            answer.append(act.split()[1] + " " + act.split()[0])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))