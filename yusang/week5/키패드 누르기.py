
def solution(numbers, hand):
    locate = {"L": 10, "R": 12}

    if hand == "right":
        hand = "R"
    else:
        hand = "L"

    answer = ""

    for num in numbers:
        if num == 0:
            num = 11
        if num in [1, 4, 7]:
            answer += "L"
            locate["L"] = num
        elif num in [3, 6, 9]:
            answer += "R"
            locate["R"] = num
        else:
            fromL = int(abs(locate["L"]-num) / 3) + \
                (abs(locate["L"] - num) % 3)
            fromR = int(abs(locate["R"]-num) / 3) + (abs(locate["R"]-num) % 3)
            if fromL == fromR:
                answer += hand
                locate[hand] = num
            elif fromL > fromR:
                answer += "R"
                locate["R"] = num
            else:
                answer += "L"
                locate["L"] = num
    return answer


print(solution(		[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
