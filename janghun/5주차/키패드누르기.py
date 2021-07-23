def solution(numbers, hand):
    L='*'
    R='#'
    answer=[]
    for i in numbers:
        if i==1 or i==4 or i==7:
            answer.append('L')
            L=i
        elif i==3 or i==6 or i==9:
            answer.append('R')
            R=i
        elif i==2:
            distance={'*':4,'#':4,0:3,1:1,2:0,3:1,4:2,5:1,6:2,7:3,8:2,9:3}
            if distance[R]>distance[L]:
                answer.append('L')
                L=i
            elif distance[R]<distance[L]:
                answer.append('R')
                R=i
            elif distance[R]==distance[L]:
                if hand=='right':
                    answer.append('R')
                    R=i
                elif hand == 'left':
                    answer.append('L')
                    L=i
        elif i==5:
            distance={'*':3,'#':3,0:2,1:2,2:1,3:2,4:1,5:0,6:1,7:2,8:1,9:2}
            if distance[R]>distance[L]:
                answer.append('L')
                L=i
            elif distance[R]<distance[L]:
                answer.append('R')
                R=i
            elif distance[R]==distance[L]:
                if hand=='right':
                    answer.append('R')
                    R=i
                elif hand == 'left':
                    answer.append('L')
                    L=i
        elif i==8:
            distance={'*':2,'#':2,0:1,1:3,2:2,3:3,4:2,5:1,6:2,7:1,8:0,9:1}
            if distance[R]>distance[L]:
                answer.append('L')
                L=i
            elif distance[R]<distance[L]:
                answer.append('R')
                R=i
            elif distance[R]==distance[L]:
                if hand=='right':
                    answer.append('R')
                    R=i
                elif hand == 'left':
                    answer.append('L')
                    L=i
        elif i==0:
            distance={'#':1,'*':1,0:0,1:4,2:3,3:4,4:3,5:2,6:3,7:2,8:1,9:2}
            if distance[R]>distance[L]:
                answer.append('L')
                L=i
            elif distance[R]<distance[L]:
                answer.append('R')
                R=i
            elif distance[R]==distance[L]:
                if hand=='right':
                    answer.append('R')
                    R=i
                elif hand == 'left':
                    answer.append('L')
                    L=i
    return(''.join(answer))


        




