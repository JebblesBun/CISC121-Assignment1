
def solution(X, Y, D):
    distance = Y - X

    jumps = (distance + D - 1) // D

    return jumps
print(solution(10,85,30))