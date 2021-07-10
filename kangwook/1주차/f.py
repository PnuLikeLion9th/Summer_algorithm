# sentenc=str(input())
# word_ilst=sentenc.split('')
# sl=int(len(word_ilst))
# answer_=[]
# for i in range(sl):
#     word = str(word_ilst[i]) #for문으로 단어 하나씩 지정
#     wl=int(len(word)) #단어 길이
#     new_word = []
#     for k in range(wl): #for문으로 단어 속 글자 하나씩 지정
#         if k%2==0:
#             new_word.append(str(word[k].upper())) #new_word 리스트에 한 글자씩 추가
#         else :
#             new_word.append(str(word[k].lower()))
#     answer_.append(str("".join(new_word))) #리스트에 있는 거 str로 출력하고 리스트에 담기 #들여쓰기 맞나?

# answer=" ".join(answer_)
# print(answer)

x,n=map(int,input().split())
answer=[]
i=1
while i <= n:
    k= x*i
    i+=1
    answer.append(str(k))
print(answer)