def solution(number, k):
    answer = []
    numbers = list(map(int ,list(reversed(number))))
    answer.append(numbers.pop())
    higher = answer[0]
    
    while numbers:
        last = numbers.pop()
        while True:
            if answer and answer[-1] < last:
                answer.pop()
                k = k - 1
            else: 
                break

            if k == 0 :
                answer.append(last)
                answer = answer + list(reversed(numbers))
                numbers = []
                break;
        answer.append(last)



    
    

    
    return str(''.join(list(map(str,answer[:-1]))))


print(solution("4177252841", 4))


#탐욕 : 지금까지 했던 것들이 옳다고 판단하고 흘러가는 알고리즘
#즉, 가장 최근의 것은 놔둔다.