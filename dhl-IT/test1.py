
def solution(S):
    occur_b = False
    for c in S:
        if occur_b and c == 'a':
            return False
        # occur_b |= c == 'b'
        if c == 'b':
            occur_b = True
    return True

def solution2(S):
    return 'ba' in S

if __name__ == '__main__':
    import timeit
    print(timeit.timeit('solution(S)', setup='from __main__ import solution; import numpy; A = numpy.random.randint(-1000000,1000000,100000)', number=10000))
    # print(solution("bb"))