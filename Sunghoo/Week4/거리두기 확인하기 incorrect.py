def check_man(p, r, c, _r, _c):
    man_dist = abs(r - _r) + abs((c - _c))
    if (man_dist > 2) or (man_dist == 0):
        print('2 or 0')
        return True
    elif man_dist ==1:
        return False
    elif man_dist == 2: # 거리가 2일 때.
        # 동일 선상 경우
        if (r == _r) or (c == _c) :
            if (c < _c) and (p[r][c + 1] == "O") or (c > _c) and (p[r][c - 1] == "O"):
                # return True
                return True
            else:
                return False
        # 대각선인 경우
        else:
            if (p[r][_c] == "O") and (p[_r][c] == "O"):
                # return True
                return True
            else:
                return False


def checkExistP(p, r, c):
    dic = {
        0: [0, 1, 2, 3, 4],
        1: [0, 1, 2, 3, 4],
        2: [0, 1, 2, 3, 4],
        3: [0, 1, 2, 3, 4],
        4: [0, 1, 2, 3, 4]
    }

    for i in dic[r]:
        for j in dic[c]:
            if not check_man(p, r, c, i, j):

                print(r, c, i, j)
                return False
    return True


def check(p):
    # p 가 나오면, 그 녀석을 기준으로 맨해튼 거리가 2 이하에 다른 p 가있는지 확인한다 => 못지키면 바로 break, false
    for row in range(5):
        for col in range(5):
            if p[row][col] == 'P':
                if not checkExistP(p, row, col):
                    print(row, col)
                    return False
            else:
                pass
    return True


def make_list(array):
    new_list = []
    for r in array:
        new_list.append(list(r))
    return new_list


def solution(places):
    answer = []
    for place in places:
        list_place = make_list(place)
        if check(list_place):
            answer.append(1)
        else:
            answer.append(0)

    return answer



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          # ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          # ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
          ]

print(solution(places))


