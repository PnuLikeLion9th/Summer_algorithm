def solution(participant, completion):
    participant.sort()  #리스트를 비교하기 위해 sort()로 정렬
    completion.sort()
    for i,j in zip(participant, completion): #두 리스트의 값을 zip()으로 확인 
        if i != j:  #만약 값이 다르면
            return i    #수가 많은 참가자쪽 데이터 반환
    return participant[-1]  #다른 값이 안나온 경우 마지막 참가자 반환