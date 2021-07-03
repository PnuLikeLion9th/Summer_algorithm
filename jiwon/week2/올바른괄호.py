def solution(s):
    stack=[] #스택 한번더(다른 방법은 효율성 검사 통과x)
    
    for i in range(len(s)):
        if s[i] is '(': # (가 나오면 스택에 추가
            stack.append(i)
        elif s[i] is ')': # )가 나오면 스택에서 뒤에꺼 지우기
            if len(stack) is 0: #지울 때 스택에 아무것도 없으면 올바르지 않은 괄호니까 False
                return False
            stack.pop()
            
    if len(stack) is not 0: #for 문 다 다돌았는데 마지막에 스택이 비어있지 않으면 False
        return False

    return True