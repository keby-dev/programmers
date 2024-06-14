import math

def solution(progresses, speeds):
    ans = []
    while len(progresses):
        l = len(progresses)
        run = math.ceil((100 - progresses[0]) / speeds[0])
        progresses = list(map(lambda x, y: x + y*run, progresses, speeds))
        while(progresses):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        ans.append(l - len(progresses))
    return ans