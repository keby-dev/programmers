import math

def solution(n):
    x = math.sqrt(n)
    return (x + 1)**2 if x.is_integer() else -1


# 라이브러리 호출 없이
# 속도가 더 빠르진 않음

def solution(n):
    x = n**(1/2)
    return (x + 1)**2 if x.is_integer() else -1