def solution(s):
    stack = [] #for, while 안쓰고 한 쪽 끝에서만 자료를 넣거나 뺄 수 있도록 제한된 선형 구조 사용
    for c in s: #주어진 s의 첫 원소 c 넣음
        if len(stack)==0:
            stack.append(c)
            continue
        if stack[-1]==c: #stack 마지막에 넣은 원소와 같으면 pop 아니면 c를 append
            stack.pop()
        else:
            stack.append(c)
    if len(stack)==0:
        return 1
    else:
        return 0