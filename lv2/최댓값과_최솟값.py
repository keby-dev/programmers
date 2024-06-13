def solution(s):
    n = [int(x) for x in s.split()]
    return "%s %s" % (min(n), max(n))