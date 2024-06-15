def solution(priorities, location):
    cnt = 0
    prior = sorted(priorities, reverse=True)
    idx = [0] * len(priorities)
    while idx[location] != 1:
        for i in range(len(priorities)):
            try:
                if idx[location] == 1:
                    break
                elif priorities[i] == prior[0] and idx[i] == 0:
                        idx[i] += 1
                        cnt += 1
                        prior.pop(0)
                        print("idx :", idx)
            except:
                break
    return print(cnt)

solution([1, 1, 9, 1, 1, 1], 0)

# enumerate 함수를 이용하여 원소와 인덱스를 함께 가져와보자!

def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer