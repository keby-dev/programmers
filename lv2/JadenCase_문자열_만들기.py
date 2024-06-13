def solution(s):
    s = s.split(' ')
    
    for i, x in enumerate(s):
        if x == '':
            continue
        else:
            s[i] = x[0].upper() + x[1:].lower()
    return ' '.join(s)

# 조건이 바뀌었지만..
# title() 함수를 사용하면 단어의 맨 앞글자를 대문자로 변환해준다..!
