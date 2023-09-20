def threeNumberSum(array, targetSum):
    array.sort()
    result_array = []
    
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            sum = array[left] + array[i] + array[right]
            if(sum == targetSum):
                result_array.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif(sum < targetSum):
                left += 1
            elif(sum > targetSum):
                right -= 1
            
    return result_array
