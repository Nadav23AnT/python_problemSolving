def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Usage example:
my_array = [5, 2, 8, 3, 1]
insertion_sort(my_array)
print(my_array)
