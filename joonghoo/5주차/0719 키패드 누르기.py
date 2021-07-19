# 프로그래머스_키패드 누르기_스택_레벨 1
# 1,4,7 ==> L , 3,6,9 ==> R 는 고정이고 손가락의 위치를 저장하여 2,5,8,0을 누를때 손가락만 생각하면 된다

def solution(numbers, hand):
    result = ""
    left_hand = 10
    right_hand = 11
    # 2,5,8,0 부터 0~9,*,# 까지의 거리를 저장한 2차원 list
    distance = [[3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4], [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3], [
        1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2], [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1]]
    for num in numbers:
        if num == 1 or num == 4 or num == 7:  # 1,4,7 일때는 왼손으로 누르고 왼손의 위치를 저장
            result += "L"
            left_hand = num

        elif num == 3 or num == 6 or num == 9:  # 3,6,9 일때는 오른손으로 누르고 오른손의 위치를 저장
            result += "R"
            right_hand = num

        else:  # 2,5,8,0 일때
            if num == 2:
                # 왼손과 오른손의 거리가 같으면 hand의 값을 통해서 키패드를 누르고 해당 손가락의 위치 저장
                if distance[0][left_hand] == distance[0][right_hand]:
                    if hand == "left":
                        result += "L"
                        left_hand = 2
                    else:
                        result += "R"
                        right_hand = 2
                # 오른손이 더 가까운경우 오른손으로 누르고 오른손 위치 저장
                elif distance[0][left_hand] > distance[0][right_hand]:
                    result += "R"
                    right_hand = 2
                else:  # 왼손이 더 가까운경우 왼손으로 누르고 왼손 위치 저장
                    result += "L"
                    left_hand = 2

            elif num == 5:
                if distance[1][left_hand] == distance[1][right_hand]:
                    if hand == "left":
                        result += "L"
                        left_hand = 5
                    else:
                        result += "R"
                        right_hand = 5
                elif distance[1][left_hand] > distance[1][right_hand]:
                    result += "R"
                    right_hand = 5
                else:
                    result += "L"
                    left_hand = 5

            elif num == 8:
                if distance[2][left_hand] == distance[2][right_hand]:
                    if hand == "left":
                        result += "L"
                        left_hand = 8
                    else:
                        result += "R"
                        right_hand = 8
                elif distance[2][left_hand] > distance[2][right_hand]:
                    result += "R"
                    right_hand = 8
                else:
                    result += "L"
                    left_hand = 8

            elif num == 0:
                if distance[3][left_hand] == distance[3][right_hand]:
                    if hand == "left":
                        result += "L"
                        left_hand = 0
                    else:
                        result += "R"
                        right_hand = 0
                elif distance[3][left_hand] > distance[3][right_hand]:
                    result += "R"
                    right_hand = 0
                else:
                    result += "L"
                    left_hand = 0
    return result


print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))
