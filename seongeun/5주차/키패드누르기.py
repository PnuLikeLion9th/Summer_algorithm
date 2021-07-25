#키패드 누르기.py
#ㄹㅇ 모르겠어요,, 이문제는 미쳤음,,
def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12

    for number in numbers :
        if number in [1,4,7] :
            left = number
            answer += 'L'
        elif number in [3,6,9] :
            right = number
            answer += 'R'
        elif number in [2,5,8,0] :
            number = 11 if number == 0 else number
            leftDist = abs(number - left)  #여기서부터 몰라서 구글링
            rightDist = abs(number - right)
            if leftDist // 3 + leftDist % 3 < rightDist // 3 + rightDist % 3 :
                left = number
                answer += 'L'
            elif leftDist // 3 + leftDist % 3 > rightDist // 3 + rightDist % 3 :
                right = number
                answer += 'R'
            elif leftDist // 3 + leftDist % 3 == rightDist // 3 + rightDist % 3 :
                if hand == 'left' :
                    left = number
                    answer += 'L'
                else :
                    right = number
                    answer += 'R'
    return answer
    
