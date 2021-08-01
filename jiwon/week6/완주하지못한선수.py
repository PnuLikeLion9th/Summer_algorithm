def solution(participant, completion):
    answer=''
    temp=0
    dic={}
    for part in participant:
        dic[hash(part)] = part 
        #hash() : 각 값에 대한 고유한 정수형 숫자를 반환해준다
        temp+=int(hash(part))
    for com in completion:
        temp -=hash(com)
    answer = dic[temp]

    return answer 