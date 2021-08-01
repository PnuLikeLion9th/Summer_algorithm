def solution(answers):
    num = [
    [1,2,3,4,5]
    ,[2,1,2,3,2,4,2,5]
    ,[3,3,1,1,2,2,4,4,5,5]]
    
    result = [0,0,0]
    
    
    for i in range(len(answers)):
        for j in range(len(num)):
            if answers[i] == num[j][i % len(num[j])]:
                result[j] += 1
            
    
    max = -1
    list = []
    for i in range(len(result)):
        if max < result[i]:
            list.clear()
            max = result[i]
            list.append(i+1)
        elif max == result[i]:
            list.append(i+1)
    
    return sorted(list)