def isValidSubsequence(array, sequence):
    j = 0
    for i in range(len(array)):
        if(sequence[j] == array[i]):
            j += 1
        if(j == len(sequence)):
            return True
    return False
