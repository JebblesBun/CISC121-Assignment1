def solution(A, K):
    if len(A) == 0:
        return A

    K = K % len(A)

    return A[-K:] + A[:-K] if K != 0 else A
print(solution([3,8,9,7,6],3))
