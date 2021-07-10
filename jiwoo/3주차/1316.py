n = int(input())

for i in range(n):
    word = input()
    for j in range(0,len(word)-1):
        if word[j] == word[j+1]:     # j번째 문자와 j+1번째 문자가 같을 경우 
            pass                    
        elif word[j] in word[j+1:]:  # j번째 문자가 j+1번째 이후로 존재할 경우 
            n -= 1                   # n을 -1 감소
            break
print(n)  # 그룹 단어 개수 출력