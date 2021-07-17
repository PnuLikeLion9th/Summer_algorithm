n = int(input())

for i in range(n):
    stack = []
    s = str(input())

    for j in range(len(s)):
        if s[j] == "(":
            stack.append(s[j])
        else:                       
            if len(stack) == 0:
                stack.append(s[j])
            elif stack[-1] =="(":   # 스택의 top이 '(' 인 경우 ')'과 합쳐 한쌍이 만들어지므로
                del stack[-1]       # '(' 삭제
    
    if len(stack) == 0:       # 스택이 비어있는 경우 (올바른 괄호열인 경우)
        print("YES")
    else:
        print("NO")