def counting_sort(arr, exp):
    # Complexity: O(n + k), where n is the number of elements and k is the range of input
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Complexity: O(d * (n + k)), where n is the number of elements, k is the range of input, and d is the number of digits in the maximum element
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Usage example:
my_array = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(my_array)
print(my_array)
