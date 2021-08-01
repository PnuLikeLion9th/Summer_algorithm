def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for par, com in zip(participant,completion): 
        if par != com :  # 같지 않다는 건, 해당 참여자가 완주자 목록에 없다는 것
            return par   # 완주하지 못한 참여자 return
        
    return participant[-1] # 중복된 값 또는 다른 값이 마지막에 있는 경우