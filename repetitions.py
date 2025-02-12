# You are given a DNA sequence: a string consisting of characters A, C, G, and
# T. Your task is to find the longest repetition in the sequence. This is a
# maximum-length substring containing only one type of character.
# Input
# The only input line contains a string of n characters.
# Output
# Print one integer: the length of the longest repetition.
# Constraints

# 1 \le n \le 10^6

# Example
# Input:
# ATTCGGGA

# Output:
# 3

def repetitions(string):
    if len(string) <= 1:
        return len(string)
    max_num = 0
    curr = 1
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            curr += 1
        else:
            max_num = max(max_num, curr)
            curr = 1

    return max(max_num,curr)

print(repetitions("ATTCGGGA"))