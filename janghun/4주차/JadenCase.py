def solution(s):
    wordlist=s.split(" ")
    #print(wordlist)
    #print(len(wordlist))
    #print(len(wordlist[0]))
    newword=''
    newwordlist=[]
    for i in range (len(wordlist)):   #단어하나하나를 부름
        for k in range (len(wordlist[i])):  #알파벳하나를 꺼냄
            getword=wordlist[i]
            alphabet=getword[k]
            #print(getword)
            #print(alphabet)
            if k == 0:
                alphabet=alphabet.upper()
            else:
                alphabet=alphabet.lower()
            newword=newword+alphabet
        newwordlist.append(newword)
        newword=''
        #print(newwordlist)
    answer=' '.join(newwordlist)
    #print(answer)
    return(answer)
