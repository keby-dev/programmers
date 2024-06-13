def solution(n):
    ans = 0
    for i in range(1, n+1):
        sum = 0
        for j in range(i, n+1):
            sum += j
            if sum == n:
                ans += 1
                break
            elif sum > n:
                break
    return ans

# 문제를 너무 어렵게 풀지 않아도 되는 경우가 있음!
# 문제 풀이 시간이 부족하면 시간 오래 걸리게 공식 사용하려고 하지 말자