def solution(numbers):
    idx = [0]*10
    for n in numbers:
        idx[n] = 1
    return sum(list(filter(lambda x: idx[x] == 0, range(len(idx)))))

# filter 함수 : 찾고자 하는 값들을 필터링 해줌

# lambda 매개변수 : 표현식


# 엥...ㅋㅋㅋ
def solution(numbers):
    return 45-sum(numbers)