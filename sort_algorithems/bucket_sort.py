def bucket_sort(arr):
    # Complexity: O(n^2) in the worst case, O(n + k) in the average case, and O(n^2) in the best case, 
    # where n is the number of elements and k is the range of input
    max_val = max(arr)
    min_val = min(arr)
    num_buckets = len(arr)
    bucket_range = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets + 1)] 

    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

# Usage example:
my_array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
my_array = bucket_sort(my_array)
print(my_array)
