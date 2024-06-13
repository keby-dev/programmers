def solution(s):
    s = list(s)
    ans = [0, 0]
    while s != '1':
        l = len(s)
        s = [i for i in s if i not in '0']
        ans[1] += l - len(s)
        s = format(len(s), 'b')
        ans[0] += 1
        
    return ans

# 코드를 좀 더 간단하게 수정

def solution(s):
    a, b = 0, 0
    while s != '1':
        cnt = s.count('1')
        b += len(s) - cnt
        s = bin(cnt)[2:] # bin 함수는 이진수 앞에 0b를 포함하여 출력하기 때문에!
        a += 1
    
    return [a, b]