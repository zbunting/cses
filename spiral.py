# A number spiral is an infinite grid whose upper-left square has number 1.
# Here are the first five layers of the spiral:

# Your task is to find out the number in row y and column x.
# Input
# The first input line contains an integer t: the number of tests.
# After this, there are t lines, each containing integers y and x.
# Output
# For each test, print the number in row y and column x.
# Constraints

# 1 \le t \le 10^5
# 1 \le y,x \le 10^9

# Example
# Input:
# 3
# 2 3
# 1 1
# 4 2

# Output:
# 8
# 1
# 15


def spiral(row,col):
    if row >= col:
        if row % 2 == 0:
            return row**2 - col + 1
        else:
            return (row-1)**2 + col
    else:
        if col % 2 != 0:
            return col**2 - row + 1
        else:
            return (col-1)**2 + row

