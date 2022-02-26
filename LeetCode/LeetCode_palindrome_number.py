# x = 12321
# x = list(str(x))
# for i in range(len(x)//2):
#     print(i, x[i], x[-(i+1)])
#     if x[i] != x[-(i+1)]:
#         print("False")
#     else:
#         print("True")
#
#
# print(x)


# class Palindrome:
#     def approach1(self, x: int) -> bool:
#         x = list(str(x))
#         for i in range(len(x) // 2):
#             if x[i] != x[-(i + 1)]:
#                 return False
#         return True
#
#     def approach2(self, x: int) -> bool:
#         pass
#
# pal = Palindrome()
# print(pal.approach1(11231))
import math

x = 12322
# x = 10000 + 2000 + 300 + 20 + 2

pwr = math.log10(x)
print(pwr)

# print(x%10)
# print((x%100 - x%10) // 10)
# print((x%1000 - x%100) // 100)