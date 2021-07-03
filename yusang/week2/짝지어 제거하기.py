
def solution(s):
    stack = []
    t = list(s)
    for e in t:
        if len(stack) > 0 and stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)
    
    return 1 if len(stack ) == 0 else 0


print(solution("baabaa"))

