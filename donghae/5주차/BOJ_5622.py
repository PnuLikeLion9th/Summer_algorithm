string = input()
#다이얼 리스트로 만들기
list = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
res = 0
for s in string:    #입력한 문자열 길이만큼
    for i in range(len(list)):                                            
        if s in list[i]:
            res += i+3  #2번 다이얼까지는 3초, 그 다음부터 1초씩 증가
print(res)