# O(n) time | O(1) space
def isMonotonic(array):
    if(len(array) == 1): return True
    isNonDecreasing = True
    isNonIncreasing = True
    
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    return isNonDecreasing or isNonIncreasing
