def solution(sentence):
    word_list=sentence.split(' ') #단어 하나씩 리스트에 담음 #split해서 쪼개니까 알아서 리스트 형식으로 담겼음!
    sl=int(len(word_list)) #단어의 개수
    answer_=[] #대문자 처리가 완료된 단어들이 담길 리스트
    for i in range(sl):
        word = str(word_list[i]) #for문으로 단어 하나씩 지정
        wl=int(len(word)) #단어 길이
        new_word = []
        for k in range(wl): #for문으로 단어 속 글자 하나씩 지정
            if k%2==0:
                new_word.append(str(word[k].upper())) #new_word 리스트에 한 글자씩 추가
            else :
                new_word.append(str(word[k].lower()))
        answer_.append(str("".join(new_word))) #리스트에 있는 거 str로 출력하고 리스트에 담기 #들여쓰기 맞나?
        
        #answer를 리스트로 저장하자. 각 단어들 대문자 처리한거 완료된거를 리스트로 담자
    answer= " ".join(answer_)
    return answer