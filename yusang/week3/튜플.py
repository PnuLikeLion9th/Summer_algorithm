def solution(s):
    answer = []
    s = s.split('},')
    s.sort(key=lambda e: len(e.split(',')))
    s = list(map(lambda e : e.replace('{','').replace('}', '').split(',') ,s))
    for e in s:
        for ee in e:
            if ee not in answer:
                answer.append(ee)
        

    return list(map(int, answer))



print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))