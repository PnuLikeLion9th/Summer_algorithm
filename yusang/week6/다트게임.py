def solution(dartResult):
    dartResult = dartResult.replace("10", "^")
    dR = list(dartResult)
    dR.reverse()
    answer = []
    
    while dR : 
        e = dR.pop()

        if e == '*' :
            try:
                answer[-1] = answer[-1] * 2
                answer[-2] = answer[-2] * 2 
            except:
                print('')
        elif e == '#' :
            try:
                answer[-1] = answer[-1] * -1
            except:
                print('')
        elif e == "S":
            print('')
        elif e == "D" :
            answer[-1] = answer[-1] * answer[-1]
        elif e == "T" :
            answer[-1] = answer[-1] * answer[-1] * answer[-1]
        else :
            if e == "^" :
                answer.append(10)
            else : 
                answer.append(int(e))
    
    return sum(answer)


print(solution("1D2S#10S"))