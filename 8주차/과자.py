#백준 파이썬 기초 50제

A, B, C = map(int, input().split())
answer = (A*B)-C 

if answer > 0:
    print(answer)
else:
    print(0)