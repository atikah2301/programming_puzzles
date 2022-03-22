## Moving Tiles

# Problem:
# Two square tiles of equal side length, L,  move at speeds s1 and s2 respectively along a the diagonal of the x-y plane
# Given a list of values for area of the overlap of the squares,
# return a list of the respective times at which the overlap takes the queried value

# Solution:
# Simply the problem by considering two dots, A and B, moving from the origin along the x axis
# Assume s2 > s1
# A has a head start on B, equal to the diagonal of the square tile from the original problem
# This diagonal length is D = sqrt(2)*L
# At any time t, A = D + s_1 * t and B = s_2 * t
# Let d be the diagonal length of the overlap square, and l be the square's side length, and q be its area
# d = A - B = sqrt(2*q)
# Rearranging and substituting, we get t = (d - D) / (s_1 - s_2)

from math import sqrt

def movingTiles(l, s1, s2, queries):
    times = []
    # apply our restriction that s2 > s1
    if s2 > s1:
        v2 = s2; v1 = s1
    else:
        v2 = s1; v1 = s2
    # calculate the times and add to the answer list
    for area in queries:
        time = (sqrt(area*2) - sqrt(2)*l) / (v1 - v2)
        if time > 0:
            times.append(time)
        else:
            times.append(0.)
    return times

if __name__ == '__main__':
    l = 10
    s1 = 1
    s2 = 2
    queries = [4, 16, 50, 99, 100, 120]
    print(movingTiles(l, s1, s2, queries))