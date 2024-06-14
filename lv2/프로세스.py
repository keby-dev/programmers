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