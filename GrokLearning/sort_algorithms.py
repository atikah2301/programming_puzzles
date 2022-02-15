# sorting algorithms
# merge sort
import data_structures
import timeit

def split(my_list: list) -> tuple:
    """
    Divide the unsorted list at its midpoint.
    Returns 2 sublists, left and right.
    A single call of split() is in constant time,
    but continuous use of split() for merge_sort() has log base 2 time
    """
    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]
    return left, right

def merge(left, right) -> list:
    """
    Merges two lists while sorting them.
    Returns a single merged list.
    Runs in linear time because for each entry in the list we need to run merge() once more
    """
    merged = []
    i = 0; j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # in case the lists are not of equal length, and one needs to continue looping
    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def merge_sort(my_list: list) -> list:
    """
    Sorts a list in ascending order.
    Returns a new sorted list.
    Since merge_sort() involve split() with O(log n) and merge() with O(n),
    the overall time complexity of merge_sort() is O(n*log n) i.e. quasilinear time
    The space complexity of merge sort is O(n) time because the final result is only as big as the input,
    and we don't store every set of sublist we created in memory, only kept one at a time.
    """

    if len(my_list) <= 1:
        return my_list

    left_half, right_half = split(my_list)  # divide
    left = merge_sort(left_half)
    right = merge_sort(right_half)  # conquer

    return merge(left, right)  # combine

def verify_sorted(my_list: list) -> bool:
    if len(my_list) > 1:
        for i in range(1,len(my_list)):
            if my_list[i] < my_list[i-1]:
                return False
    return True

def merge_sort(my_linked_list):
    pass


print(split([1, 2, 3, 4, 5, 6]))
print(merge([31,21,4],[14,6,20]))
listA = [3,91,17,82,5,6]
print(merge_sort(listA))
print(verify_sorted(merge_sort(listA)))
print(verify_sorted([1,2,4,3]))

print(timeit.timeit(()))