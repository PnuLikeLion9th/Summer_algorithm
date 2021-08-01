def solution(answers):
    answer = [0 for i in range(3)]

    man1 = [1,2,3,4,5]                  # 수포자들의 찍기 방식을 리스트로 생성
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):       # 찍을 숫자와 정답이 같은 경우 맞춘 횟수를 올려주기
        ans = answers[i]
        if(man1[i%len(man1)] == ans):
            answer[0] += 1
        if(man2[i%len(man2)] == ans):
            answer[1] += 1
        if(man3[i%len(man3)] == ans):
            answer[2] += 1     
    
    result = []
    for i in range(len(answer)):
        if(answer[i] == max(answer)):
            result.append(i+1)
    
    return sorted(result)