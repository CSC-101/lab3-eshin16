more = [x + 1 for x in [1,2,3,4]]         # The values x takes at each step: 1, 2, 3, 4
print(more)                               # The value of more is [2, 3, 4, 5]

#############################################################################################################
def square(n:int) -> int:
    return n * n                           # n = 1 -> 1
                                           # n = 2 -> 4
                                           # n = 3 -> 9
                                           # n = 4 -> 16


squares = [square(x) for x in [1,2,3,4]]   # squares = [1, 4, 9, 16], it is related to the values above because it's each of the values of n squared
print()
#############################################################################################################
def check(n:int) -> bool:
    return n > 2                             # n = 0 -> False
                                             # n = 1 -> False
                                             # n = 2 -> False
                                             # n = 3 -> True
                                             # n = 4 -> True


answer = [x for x in range(5) if check(x)]   # The value of answer is [3,4]
print()
#############################################################################################################
def inc(m:int) -> int:
    return m + 1                             # m = 0 -> 1
                                             # m = 1 -> 2
                                             # m = 2 -> 3
                                             # m = 3 -> 4
                                             # m = 4 -> 5

def check(n:int) -> bool:
    return n > 2                             # n = 0 -> False
                                             # n = 1 -> False
                                             # n = 2 -> False
                                             # n = 3 -> True
                                             # n = 4 -> True


answer = [inc(x) for x in range(5) if check(x)]   # The value of answer is [4, 5]
print()
