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

def pascalsRow(row):
    # counting rows from 0
    values = []
    for col in range(row+1):
        values.append(pascalsTriangle(row, col))
    return values

def pascalsRowRatios(row):
    # counting rows from 0
    values = []
    for column in range(row + 1):
        pascal = pascalsTriangle(row, column)
        values.append(pascal/(2**row))
    return values

def ceil(num):
    if num != int(num):
        return int(num)+1.0
    else:
        return num

def pascalsRowThreshold(row):
    # counting rows from 0
    values = []
    for column in range(row + 1):
        pascal = pascalsTriangle(row, column)
        values.append(ceil((2 ** row) / pascal))
    return values

def cupsNeeded(n):
    cups_needed_to_fill_tower = [[1.0]]
    row = [1.0]
    for i in range(n): # for each row
        next_row = pascalsRowThreshold(i+1)
        for j in range(0, len(next_row)//2): # for the first half of values in current row
            next_row[j] = next_row[j] + row[j]
        for j in range(len(next_row)//2, len(next_row)): # for the second half
            next_row[j] = next_row[j] + row[j-1]
        cups_needed_to_fill_tower.append(next_row)
        row = next_row
    return cups_needed_to_fill_tower

def printPascalsTriangle(row):
    for i in range(row+1):
        for j in range(row-i+1):
            print(" ", end="")
        for j in range(i+1):
            print(pascalsTriangle(i,j), end=" ")
        print("")

def champagneTower(poured, query_row, query_glass):
    cups_needed = cupsNeeded(query_row)[query_row][query_glass]
    print(cups_needed)
    if poured >= cups_needed:
        return 1.0
    else:
        ratio = pascalsRowRatios(query_row)[query_glass]
        fill = 1 - ratio*(cups_needed - poured)
        if fill <= 0:
            return 0.0
        else:
            return fill

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
    poured = 6
    query_row = 3
    query_glass = 3 # query_glass <= query_row < 100
    # for i in range(0, query_row+3):
    #     print(f"row {i}: ", end=" ")
    #     for _ in range(query_row, i-2, -1):
    #         print("  ", end="")
    #     for j in range(0, i+1):
    #         print(sol.champagneTower(poured, i, j), end=" ")
    #     print()
    #print(sol.champagneRemaining(poured))

    # tower = []
    # for i in range(5):
    #     tower.append(pascalsRowThreshold(i))
    # print(tower)

    print(champagneTower(poured, query_row, query_glass))




