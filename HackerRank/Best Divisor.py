import math


def get_divisors(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def split_by_digits(k):
    length = int(math.log(k, 10)) + 1
    digits = []
    for i in range(length):
        digits.append(((k % 10 ** (i + 1)) - (k % 10 ** i)) // 10 ** i)
    digits.reverse()
    return digits


def best_number(nums):


def best_divisor(n):
    divisors = get_divisors(n)
    split_divisors = []
    for divisor in divisors:
        split_divisors.append(split_by_digits(divisor))
    for split_divisor in split_divisors:


n = 156
# print(get_divisors(n))
# print(split_by_digits(n))
# get divisors of n
# for each divisor, split it into its digits
# for each of the split numbers, calculate their sum
# find the largest sum
# if the sum is unique, return the number that gave that sum
# if the sum is not unique,
# return the smallest number among those that gave the largest sum
