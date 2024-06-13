def solution(A,B):
    A.sort()
    B.sort(reverse = True)

    return sum([a*b for a, b in zip(A, B)])

# return에서 sort() 함수를 적용했을 때 오류가 난 이유
#   : sort() 함수는 정렬 후, 리스트를 영구 수정하면서 'None'을 반환
#     반면에 sorted() 함수는 정렬한 리스트를 저장하지는 않으나
#     정렬된 목록만을 반환하기 때문에 아래 함수와 같이 수정

def solution(A,B):
    return sum([a*b for a, b in zip(sorted(A), sorted(B, reverse = True))])