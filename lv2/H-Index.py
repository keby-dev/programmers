# 1. 인용 횟수 기준 오름차순 정렬
# 2. 최대 값을 찾기 위해 상위 값부터 계산
# 3. 추정한 h 값 검증
#       1) h 이상의 요소 개수
#       2) h 이하의 요소 개수

def solution(citations):
    citations.sort()
    n = len(citations)
    for h in range(citations[-1], 0, -1):
        h_list = list(filter(lambda x: x >= h, citations))
        if len(h_list) >= h and len(citations) - len(h_list) <= h:
            return h

solution([3, 0, 6, 1, 5])