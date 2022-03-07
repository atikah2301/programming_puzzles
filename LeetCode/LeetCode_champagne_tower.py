# Medium difficulty

# Glasses are stacked in rows, in a triangle structure
# Each glass holds 1 cup of champagne
# There is 1 glass in the first row, 2 glasses in the second row etc.
# n cups of champagne are poured into the top glass
# Once filled, the excess champagne fill the glasses beneath

# i = row:  0, 1, .., 99
# j = glass: 0, 1, .., i

def factorial(n):
    if n == 0:
        return 1
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def pascalsTriangle(row, col):
    if col < 0 or row < 0 or col > row:
        return 0
    top = factorial(row)
    bottom = factorial(col)*factorial(row-col)
    #print(f"{top} / {bottom}")
    return int(top/bottom)

def printPascalsTriangle(row):
    for i in range(row+1):
        for j in range(row-i+1):
            print(" ", end="")
        for j in range(i+1):
            print(pascalsTriangle(i,j), end=" ")
        print("")

class Solution:
    def champagneRemaining(self, poured: int):
        remainder = poured
        i = 1  # number of rows with all glasses filled by the amount poured
        while remainder - i >= 0:  # fill up entire rows of glasses, one row at a time
            remainder -= i
            i += 1
        return i-1, remainder

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        rows_filled, remainder = self.champagneRemaining(poured)

        if query_row <= rows_filled - 1: # if you queried a glass in the full rows
            return 1.0
        elif remainder > 0 and rows_filled == query_row: # if you queried a glass in the partially filled row
            pascal_row_sum = 2**(query_row)
            query_glass_fill_ratio = pascalsTriangle(query_row, query_glass)
            proportion_filled = remainder * query_glass_fill_ratio / pascal_row_sum
            return proportion_filled
            # if proportion_filled <= 1.0:
            #     return proportion_filled
            # else:
            #     return 1.0
        else: # if you queried a glass in an empty row, or a glass that doesn't exist
            return 0.0


if __name__ == '__main__':
    sol = Solution()
    poured = 104
    query_row = 14
    query_glass = -1 # query_glass <= query_row < 100
    for i in range(0, query_row+3):
        print(f"row {i}: ", end=" ")
        for _ in range(query_row, i-2, -1):
            print("  ", end="")
        for j in range(0, i+1):
            print(sol.champagneTower(poured, i, j), end=" ")
        print()
    #print(sol.champagneRemaining(poured))

    # Tests

    # 1. Full glass
    # rows are completely full for poured = 1, 3, 6, 10, 15, 21
    # for query_row = 0, 1, 2, 3, 4, 5  and below respectively

    # Example: poured, row, glass = 6, 2, 0 -- then return 1.0

    # 2. Partially full glass
    # rows are partially full for poured != the values above
    # the partially filled row will be last filled query_row + 1

    # Example: poured, row, glass = 7, 4, 2 -- then return 1.0

    # 3. Empty glass
    # rows are empty for query_row > last filled row for poured value == above,
    # but empty only for query_row + 1 > last filled row for poured value != above

