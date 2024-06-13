import numpy

def solution(absolutes, signs):
    ans = 0
    for i in range(len(signs)):
        if signs[i] == True:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]
    return ans


# zip 함수 : 두 그룹의 데이터를 엮음
def solution(absolutes, signs):
    ans = 0
    for a, s in zip(absolutes, signs):
        if s:
            ans += a
        else:
            ans -= a
    return ans
