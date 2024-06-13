# 완전 탐색(Brute Force)
#   : 모든 경우의 수를 다 체크해서 정답을 찾는 방법
#     1) 가능한 경우의 수를 대략적으로 계산
#     2) 가능한 모든 방법을 다 고려
#           - Brute Force 기법
#           - 순열
#           - 재귀 호출
#           - 비트마스크(2진수 표현 기법 활용)
#           - BFS, DFS를 활용

def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2)+1)):
        w, h = 0, 0
        if yellow % i == 0:
            w = yellow / i
            h = i
            if (w+h)*2 + 4 == brown:
                return [w+2, h+2]


# 불필요한 변수 선언 줄이기

def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2)+1)):
        if yellow % i == 0:
            w = yellow / i
            h = i
            if (yellow/i + i) * 2 + 4 == brown:
                return [yellow / i+2, i+2]