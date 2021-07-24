def solution(s):
    strs=["zero","one","two","three","four","five","six","seven","eight","nine"]
    num=['0','1','2','3','4','5','6','7','8','9']   #각 다른 리스트로 문자와 숫자 배열
    for i in range(10):
        if strs[i] in s:    #주어진 것에 문자열이 있으면 그거에 맞는 숫자로 바꿈
            s=s.replace(strs[i],num[i])
    return int(s)