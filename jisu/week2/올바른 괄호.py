# 프로그래머스 레벨2
def solution(s):
    stack = []

    for i in s:  # 열린 괄호일 경우 stack에 append, 닫는 괄호일 경우 stack에서 pop
        if(i == '('):
            stack.append('(')
        else:
            try:
                stack.pop()
            except IndexError:  # 닫는 괄호가 맨앞에 나올경우 IndexError 발생. 이 경우는 올바르지 않은 괄호이므로 False 반환
                return False

    # stack에 괄호가 남아있으면(개수가 1이상일 경우), False 반환
    return False if len(stack) > 0 else True
