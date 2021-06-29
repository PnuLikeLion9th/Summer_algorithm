A = int(input())
B = int(input())
C = int(input())
sum = str(A*B*C)
for i in range(10): 
    print(sum.count(str(i)))    #숫자가 등장한 횟수만큼 출력