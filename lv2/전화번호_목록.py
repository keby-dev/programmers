def solution(phone_book):
    p_hash = {}
    for i in phone_book:
        p_hash[i] = 1
    
    for num in phone_book:
        arr = ""
        print("num: ", num)
        for j in num:
            print("j: ",j)
            arr += j
            if arr in p_hash and arr != num:
                return False
    return True