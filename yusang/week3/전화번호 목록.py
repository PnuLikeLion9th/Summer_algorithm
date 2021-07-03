def solution(phone_book):
    phone_book.sort()
    phone_book.reverse()

    while len(phone_book) > 1:
        target = phone_book.pop()
        if phone_book[-1].startswith(target) == True:
            return False
    
    return True