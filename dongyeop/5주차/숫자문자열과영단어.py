# def solution(s):
#     checklist = ['zero','one','two','three','four','five','six','seven','eight','nine']
#     numberlist = ['0','1','2','3','4','5','6','7','8','9']
#     check = ""
#     answer = ""
#     for i in s:
#         if i in numberlist:
#             answer+=i
#         else:
#             check+=i
#             if check in checklist:
#                 for i in range(len(checklist)):
#                     if checklist[i] == check:
#                         answer+=str(i)
#                         check = ""
#                         break
        
#     return int(answer)
#위에는 리스트로 푼거 아래는 딕셔너리로 풀기
def solution(s):
    answer = s
    dic_items = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    for key,value in dic_items.items():
        answer = answer.replace(key,value)#바꿔바꿔~~
    return int(answer)
solution('seven12three4')