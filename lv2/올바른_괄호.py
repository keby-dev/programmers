def is_match(l, r):
    if l == r:
        l, r = 0, 0
        return True
    elif l > r:
        return False
    
def solution(s):
    chk = True
    l_chk = 0
    r_chk = 0
    s = list(s)
    print(s)

    for i in range(len(s)):
        if s[0] == ')' or (is_match(l_chk, r_chk) and s[-1] == '('):
            return print(False)
        elif s[-1] == ')':
            s.pop()
            r_chk += 1
            is_match(l_chk, r_chk)
        elif s[-1] == '(':
            s.pop()
            l_chk += 1
            is_match(l_chk, r_chk)

    return print(True)


# 새로운 알고리즘..!
# 예외처리를 이용하는 깔끔한 방식

def solution(s):
    st = list()
    for c in s:
        if c == '(':
            st.append(c)

        if c == ')':
            try:
                st.pop()
            except IndexError:
                return False

    return len(st) == 0