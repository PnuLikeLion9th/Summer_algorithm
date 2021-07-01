def solution(phone_number):
    return len(phone_number[:-4])*'*'+phone_number[-4:]#4자리 전까지의 길이에 *을 곱해주고 그 뒤에 끝에서 4자리부터를 붙여준다.