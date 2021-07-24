# from collections import deque
# n = int(input())
# stack = list()
# answer = ''
# q = deque(i for i in range(1,n+1))
# for i in range(n):
#     want_pop= int(input())
#     if stack:
#         if stack[-1]>=want_pop:
#             if want_pop in stack:
#                 while stack[-1]>want_pop:
#                     stack.pop()
#                     answer+='-'
#                 stack.pop()
#                 answer+='-'
#             else:
#                 answer = 'NO'
#                 break
#         elif stack[-1]<want_pop:
#             if want_pop in q:
#                 while stack[-1]<want_pop:
#                     stack.append(q.popleft())
#                     answer+='+'
#                 stack.pop()
#                 answer+='-'
#             else:
#                 answer = 'NO'
#                 break
#     else:
#         for i in range(want_pop):
#             stack.append(q.popleft())
#             answer+='+'
#         stack.pop()
#         answer+='-'
# if answer != 'NO':
#     for i in answer:
#         print(i)
# else:
#     print(answer)

#계속 틀려서 풀이보고함 문제를 제대로 이해하고 풀이에 접근해야할듯..이렇게 간단히 풀리는걸..
n = int(input())
s = []
op = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count<=num:
        s.append(count)
        op.append('+')
        count+=1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        temp = False
if temp == False:
    print('NO')
else:
    for i in op:
        print(i)