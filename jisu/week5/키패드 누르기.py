def solution(numbers, hand):
    answer = ''
    
    keypad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    left_curr = '*'
    right_curr = '#'
    
    for i in numbers:
        if i in [1,4,7]: #규칙2
            answer += 'L'
            left_curr = i
        elif i in [3,6,9]: #규칙3
            answer += 'R'
            right_curr = i
        else: 
            curPos = keypad[i]
            leftPos = keypad[left_curr]
            rightPos = keypad[right_curr]

            #맨하탄 거리 계산법
            ldist = abs(curPos[0]-leftPos[0]) + abs(curPos[1]-leftPos[1])
            rdist = abs(curPos[0]-rightPos[0]) + abs(curPos[1]-rightPos[1])
            
            if ldist < rdist: #규칙4
                answer += 'L'
                left_curr = i
            elif ldist > rdist: #규칙4
                answer += 'R'
                right_curr = i
            else: #규칙4-1
                if hand == 'left':
                    answer += 'L'
                    left_curr = i
                else:
                    answer += 'R'
                    right_curr = i
    
    return answer