n = int(input())
stack = []
result = []   # 결과 값 담아줄 리스트
count = 1
a = True

for i in range(n):
    num = int(input())

    while count <= num :
        stack.append(count)   # 스택에 1부터 차곡차곡 담음
        result.append('+')    # count, num 같아질 때까지 result에 + 담기
        count += 1

    if stack[-1] == num:      # 스택의 마지막 값과 num이 같다면,
        stack.pop()           # 스택에서 pop하고
        result.append('-')    # result에 - 담기
    else:             
        a = False
        break

if a == False:                # 불가능한 경우
    print("NO")
else:
    for i in result:
        print(i)              # result에 담긴 값 출력