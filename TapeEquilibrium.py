
def solution(A):
    total_sum = sum(A)
    left_sum = 0
    min_difference = float('inf')

    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum

        difference = abs(left_sum - right_sum)

        min_difference = min(min_difference, difference)

    return min_difference
print(solution([3,1,2,4,3]))