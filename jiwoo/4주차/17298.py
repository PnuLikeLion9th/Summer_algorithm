n = int(input())
stack = []           # 원소의 인덱스 값을 넣어줄 스택
result = [-1] * n

a = list(map(int,input().split()))

stack.append(0)      # 처음 인덱스 값 = 0 을 스택에 추가
for i in range(1,n):
    while stack and a[stack[-1]] < a[i]:  # 스택의 마지막 값을 인덱스로 해서 a[i]보다 작을 경우에,
        result[stack.pop()] = a[i]        # pop 해주고, result의 pop한 인덱스 값에 오큰수인 a[i] 담아줌
    stack.append(i)                       

for i in result:
    print(i, end=' ') 