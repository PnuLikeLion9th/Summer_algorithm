# 문제 : 프로그래머스 2017 팁스다운
# 난이도 : Lv2
# 풀이 : https://breathtaking-life.tistory.com/120

def solution(s):
    stack = []
    for c in s:
        # 스택에 문자가 하나 이상 있으면서 스택 맨위의 문자와 c가 같다면
        if len(stack) > 0 and stack[-1] == c:
            stack.pop()  # 스택 맨 위 비워줌
            continue  # c가 stack에 들어가지 않게 continue
        stack.append(c)
    return 0 if len(stack) else 1
