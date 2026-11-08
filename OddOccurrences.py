
def solution(A):
    result = 0

    for num in A:
        result ^= num

    return result
print(solution([9,3,9,3,9,7,9]))