# Memoisation for Dynamic Programming

# def fib(n):
#     if n <= 2: return 1
#     return fib(n-1) + fib(n-2)

memo = {}
def fib(n, memo):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

if __name__ == '__main__':
    for e in [6]:
        print(fib(e, memo))
    print(memo)
