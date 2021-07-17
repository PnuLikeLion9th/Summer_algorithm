def solution(s):
    word=s.split() #word=['hello', 'hello', 'world']
    #print(word) 
    #word[0]='first' #word[0]인자 바꿀수 있는지 실험
    #print(word)
    #print(len(word)) #word 리스트의 길이
    #print (len(word[0])) #word 리스트의 0번째 인자의 길이
    newwordlist=[]
    newword=''
    for i in range(0,len(word)):     #리스트 안의 단어를 하나씩 호출
        for m in range(0,len(word[i])):     #단어를 하나씩 호출해서 알파벳 하나씩 부르기
            middelword=word[i]             #단어하나를 꺼내서 middelword에 넣어줬어
            alphabet=middelword[m]
            #print(alphabet)           #middelword의 글자하나하나를 프린트
            #print(m)
            if m%2==0:                  #alphabet이 짝수번째면 대문자로 바꿔라
                alphabet=alphabet.upper()
            #print(alphabet)
            newword=newword+alphabet    #알파벳을 합친 newword라는 단어를 만들어준다.
        #print(newword)                  
        newwordlist.append(newword)     #만들어진 newword를 newwordlist에 추가한다.
        newword=''                      #newword를 초기화 해준다.
        #print(newwordlist)
    answer=(' '.join(newwordlist))
    return answers