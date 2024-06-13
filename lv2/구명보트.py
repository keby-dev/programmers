# 1. 최대 몸무게부터 태우기
# 2. 최대+최소 몸무게가 무게제한과 같거나 작은지 확인 -> 짝지어 빼기
# 3. 아니라면 최대 몸무게는 따로 빼기

import math

def solution(people, limit):
    people.sort()
    cnt = 0
    min, max = 0, len(people)-1
    
    if people[-1] <= limit/2:
        return math.ceil(len(people)/2)
    else:
        while min <= max:
            if people[min] + people[max] <= limit:
                min += 1
                max -= 1
            else:
                max -= 1
            cnt += 1
        return cnt

    
# 불필요한 것 줄이기

def solution(people, limit):
    people.sort()
    cnt = 0
    min, max = 0, len(people)-1
    
    while min <= max:
        if people[min] + people[max] <= limit:
            min += 1
            max -= 1
        else:
            max -= 1
        cnt += 1
    return cnt