#키패드 누르기 

def solution(numbers, hand):
    answer = ''
    
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    left_s = dic['*']
    right_s = dic['#']
    
    for i in numbers:
        now = dic[i]
        if i in [1, 4, 7]: #왼손
            answer += 'L'
            left_s = now
   
        elif i in [3, 6, 9]: #오른손
            answer += 'R'
            right_s = now
            
        else:   #남는애들
            left_d = 0
            right_d = 0
            
            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            
            if left_d < right_d:  #왼손 가까울 떄
                answer += 'L'
                left_s = now
                
            elif left_d > right_d: #오른손 가까울 때
                answer += 'R'
                right_s = now
            
            else:  #거리가 같을 때 
                if hand == 'left':
                    answer += 'L'
                    left_s = now
                    
                else:
                    answer += 'R'
                    right_s = now
            
    return answer