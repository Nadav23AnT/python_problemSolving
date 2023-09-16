# o(nlogn)
def sortedSquaredArray(array):
    arr = [0 for _ in array]
    for i in range(len(array)):
        arr[i] = pow(array[i], 2)
    arr.sort()
    return arr
