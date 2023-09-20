# def getNthFib(n, memoize = {1:0 , 2:0}):
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2 , memoize)
#         return memoize[n]

def getNthFib(n):
    lastTwo = [0 , 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]