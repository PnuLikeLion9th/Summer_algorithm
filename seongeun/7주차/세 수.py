#백준 50제-세 수
# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 

A= list(map(int,input().split()))
A.sort()
print(A[1]) 
