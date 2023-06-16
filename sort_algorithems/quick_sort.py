def quick_sort(arr):
    # Complexity: O(n^2) in the worst case, O(n log n) in the average case, and O(n log n) in the best case
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Usage example:
my_array = [5, 2, 8, 3, 1]
my_array = quick_sort(my_array)
print(my_array)
