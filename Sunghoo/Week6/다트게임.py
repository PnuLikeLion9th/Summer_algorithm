def solution(dartResult):
    temp = []
    for idx, letter in enumerate(dartResult):
        if idx == 0 and letter == '0':
            temp.append(0)
            continue

        try:

            if letter == '0' and temp[-1] == 1:
                temp.pop()
                temp.append(10) # 이전의 1은 제거해줘야한다.
                continue
            elif letter == '0' and temp[-1] != 1:
                pass
            letter = int(letter)
            temp.append(letter)

        except:
            num = temp.pop()
            if letter == "D":
                num = num ** 2
                temp.append(num)
            elif letter == 'T':
                num = num ** 3
                temp.append(num)
            elif letter == 'S':
                temp.append(num)

            try:
                if letter == '*' and temp:
                    num = num * 2
                    num2 = temp.pop() * 2
                    temp.append(num2)
                    temp.append(num)
                elif letter == '*' and not temp:
                    num = num * 2
                    temp.append(num)
                elif letter == '#':
                    num = num * (-1)
                    temp.append(num)
            except IndexError:
                pass
    return sum(temp)
