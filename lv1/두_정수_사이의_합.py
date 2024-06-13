def solution(a, b):
    if a > b:
        a, b = b, a
    return sum(i for i in range(a, b+1))


# 수학식을 활용해보자
def solution(a, b):
    return (abs(a-b)+1)*(a+b)/2
