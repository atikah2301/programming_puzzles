## Minimum number of ways to cut paper into 1x1 unit sqaure pieces

# "Cutting Paper Sqaures" fro mHackerRank > Mathematics > Fundamentals

def solve(n, m):
    # Let a be the bigger of n and m and b be the smaller
    if n >= m:
        a,b = n,m
    else:
        a,b = m,n

    # first we cut out b strips on the shortest side, by making b-1 cuts
    # as this cuts the longest lines in one go
    # then for each of our b strips we need to make (a-1) cuts
    
    return (b-1) + (a-1)*b
