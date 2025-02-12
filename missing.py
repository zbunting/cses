# You are given all numbers between 1,2,\ldots,n except one. Your task is to
# find the missing number.
# Input
# The first input line contains an integer n.
# The second line contains n-1 numbers. Each number is distinct and between 1
# and n (inclusive).
# Output
# Print the missing number.
# Constraints

# 2 \le n \le 2 \cdot 10^5

# Example
# Input:
# 5
# 2 3 1 5

# Output:
# 4

def missing(n, nums):
    n_sum = n*(n+1)/2
    curr_sum = 0
    for num in nums:
        curr_sum += num

    return n_sum - curr_sum

print(missing(5, [2,3,1,5]))