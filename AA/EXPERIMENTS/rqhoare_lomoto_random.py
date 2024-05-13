import random
import time

def partition_lomuto(arr, low, high):
    if low < high:
        start = low - 1
        pivot = high
        for end in range(low, high):
            if arr[end] <= arr[pivot]:
                start += 1
                arr[start], arr[end] = arr[end], arr[start]
        arr[start + 1], arr[high] = arr[high], arr[start + 1]
        p = start + 1
        partition_lomuto(arr, low, p - 1)
        partition_lomuto(arr, p + 1, high)
        
def partition_lomuto_random(arr, low, high):
    if low < high:
        k = random.randint(low, high)
        arr[k], arr[high] = arr[high], arr[k]
        start = low - 1
        pivot = high
        for end in range(low, high):
            if arr[end] <= arr[pivot]:
                start += 1
                arr[start], arr[end] = arr[end], arr[start]
        arr[start + 1], arr[high] = arr[high], arr[start + 1]
        p = start + 1
        partition_lomuto_random(arr, low, p - 1)
        partition_lomuto_random(arr, p + 1, high)
        
def partition_hoare(arr, low, high):
    if low < high:
        start = low
        end = high
        pivot = low
        while start < end:
            while arr[start] <= arr[pivot] and start < high:
                start += 1
            while arr[end] > arr[pivot]:
                end -= 1
            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
        arr[end], arr[pivot] = arr[pivot], arr[end]
        partition_hoare(arr, low, end - 1)
        partition_hoare(arr, end + 1, high)
        
def partition_hoare_random(arr, low, high):
    if low < high:
        k = random.randint(low, high)
        arr[k], arr[low] = arr[low], arr[k]
        start = low
        end = high
        pivot = low
        while start < end:
            while arr[start] <= arr[pivot] and start < high:
                start += 1
            while arr[end] > arr[pivot]:
                end -= 1
            if start < end:
                arr[start], arr[end] = arr[end], arr[start]
        arr[end], arr[pivot] = arr[pivot], arr[end]
        partition_hoare_random(arr, low, end - 1)
        partition_hoare_random(arr, end + 1, high)

random_array = [i for i in range(500)[::-1]]
random_array1 = random_array.copy()
random_array2 = random_array.copy()
random_array3 = random_array.copy()
# Timing Lomuto Quicksort
start_time = time.time()
partition_lomuto(random_array, 0, len(random_array) - 1)
end_time = time.time()
print("Lomuto Quicksort Time:", end_time - start_time)

# Timing Lomuto Quicksort with random pivot selection
start_time = time.time()
partition_lomuto_random(random_array1, 0, len(random_array1) - 1)
end_time = time.time()
print("Lomuto Quicksort with Random Pivot Selection Time:", end_time - start_time)

# Timing Hoare Quicksort
start_time = time.time()
partition_hoare(random_array2, 0, len(random_array2) - 1)
end_time = time.time()
print("Hoare Quicksort Time:", end_time - start_time)

# Timing Hoare Quicksort with random pivot selection
start_time = time.time()
partition_hoare_random(random_array3, 0, len(random_array3) - 1)
end_time = time.time()
print("Hoare Quicksort with Random Pivot Selection Time:", end_time - start_time)