def solution(x, n):
    return list(i for i in range(x, x*(n+1), x))


# 생각의 전환을 하자!
# 핵심은 등차수열
def solution(x, n):
    return  [i * x + x for i in range(n)]