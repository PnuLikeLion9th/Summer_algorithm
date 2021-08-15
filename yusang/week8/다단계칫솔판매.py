import math
 
def solution(enroll, referral, seller, amount):
    parentTree = dict(zip(enroll, referral))
    print(parentTree)
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))    
    for i in range(len(seller)):
        earn = amount[i] * 100
        target = seller[i]
        while True :
            if earn < 10 : #10원 단위 이하라면 모두 받고 레퍼럴 종료
                answer[target] += earn
                break
            else : #10% 레퍼럴을 제외하고 받는다
                answer[target] += math.ceil(earn * 0.9)
                if parentTree[target] == "-": #상위가 없다면 종료
                    break
                earn = math.floor(earn*0.1)
                target = parentTree[target]
                    
    return list(answer.values())