A, B = input(), split()

answer = []
for i in range(len(B)-len(A)+1):       # B가 A보다 크거나 같아 +1을 해줌.
    count = 0
    for j in range(len(A)):           
        if A[j] != B[i+j]:             # A와 B가 같지 않은 경우
            count += 1                 # count를 1씩 더하기
    answer.append(count)               # answer라는 리스트에 더함.

print(min(answer))                     # answer 리스트 중 최솟값 구하기