def solution(numbers, hand):
    phone = [[1,4,7,"*"],[2,5,8,0],[3,6,9,"#"]]#핸드폰 왼쪽 중단 오른쪽으로 나눔
    answer = []
    right_hand = ["#"]#현재 오른손의 위치
    left_hand = ["*"]#현재 왼손으 위치
    for i in numbers:
        if i in phone[0]:#번호가 1,4,7이면 왼손추가
            answer.append('L')
            left_hand.append(i)
        elif i in phone[2]:#번호가 3,6,9이면 오른손 추가
            answer.append("R")
            right_hand.append(i)
        elif i in phone[1]:#번호가 2,5,8,0이면
            check = phone[1].index(i)#몇번쨰인지 체크
            if left_hand[-1] in phone[0]:#왼손이 147*에 있으면
                left_handl = abs(phone[0].index(left_hand[-1])-check)+1#세로이동에다 가로 이동 하나만큼 더해줌
            elif left_hand[-1] in phone[1]:#같은곳에 있으면
                left_handl = abs(phone[1].index(left_hand[-1])-check)#세로이동만 계산
            if right_hand[-1] in phone[2]:#오른손이 369#에 있으면
                right_handl = abs(phone[2].index(right_hand[-1])-check)+1#세로이동에다 가로 이동 하나만큼 더해줌
            elif right_hand[-1] in phone[1]:#같은곳에 있으면
                right_handl = abs(phone[1].index(right_hand[-1])-check)#세로이동만 계산
            if right_handl>left_handl:#오른손의 이동이 왼손의 이동보다 많으면 왼손을 답에 추가
                answer.append("L")
                left_hand.append(i)
            elif right_handl<left_handl:#왼손이 오른손의 이동보다 많으면 오른손을 답에 추가
                answer.append("R")
                right_hand.append(i)
            else:#같으면 hand값에 따라 달라짐
                if hand == "right":
                    answer.append("R")
                    right_hand.append(i)
                else:
                    answer.append("L")
                    left_hand.append(i)
    return "".join(answer)