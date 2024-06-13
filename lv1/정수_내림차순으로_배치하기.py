def solution(n):
    n = list(map(str,str(n)))
    n.sort(reverse = True)
    n = ''.join(n)
    return int(n)

# 줄인 코드
def solution(n):
    n = list(str(n))
    n.sort(reverse = True)
    return int(''.join(n))