## Reverse Diagonal

# Write a function that traverses an NxN (i.e. square) matrix
# in reverse diagonal order, and prints each element
# Sample input and output shown below

# input:
# 123
# 456
# 789

# output: 3,2,6,1,5,9,4,8,7

def reverse_diagonal(M):
    n = len(M[0])

    for x in range(n + 1):
        # print(f"x = {x} / {n}")
        for y in range(x):
            print(M[y][y - x + n])
            # print(f"\t y = {y} / {x-1} ->", end=" ")
            # print(f"{(y, y-x+n)}")

    for x in range(n - 1, 0, -1):
        # print(f"x = {x} / {n}")
        for y in range(x):
            print(M[y - x + n][y])
            # print(f"\t y = {y} / {x-1} ->", end=" ")
            # print(f"{(y-x+n, y)}")

# Testing with 3x3 and 4x4 matrices

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# M = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

reverse_diagonal(M)