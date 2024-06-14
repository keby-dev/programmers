def solution(clothes):
    ans = 1
    ctype = {}
    for x in clothes:
        if x[1] not in ctype.keys():
            ctype[x[1]] = 1
        else:
            ctype[x[1]] += 1
    for v in ctype.values():
        ans *= int(v)+1
    
    return print(ans)

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])