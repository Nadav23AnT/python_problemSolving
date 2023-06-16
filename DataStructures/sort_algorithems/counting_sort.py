def counting_sort(arr):
    max_val = max(arr) + 1
    count = [0] * max_val

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i in range(max_val):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

# Usage example:
my_array = [5, 2, 8, 3, 1]
my_array = counting_sort(my_array)
print(my_array)
