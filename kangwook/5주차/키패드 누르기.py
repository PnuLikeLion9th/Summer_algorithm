def solution(numbers,hand):
    answer=""
    hL=10 # *=10
    hR=12 # #=12
    for i in numbers:
        if i == 1 or i == 4 or i == 7: 
            answer+='L'
            hL=i
        elif i == 3 or i == 6 or i == 9: 
            answer+='R'
            hR=i
        else:
            if i ==0: i=11
            LL=abs(hL-i)//3+abs(hL-i)%3     #거리계산. 키패드가 3개씩 있다는 것을 활용
            RR=abs(hR-i)//3+abs(hR-i)%3
            if LL<RR:
                answer+='L'
                hL=i
            elif LL==RR:
                if hand=='left':
                    answer+='L'
                    hL=i
                else:
                    answer+='R'
                    hR=i
            elif LL>RR:
                answer+='R'
                hR=i
    return answer