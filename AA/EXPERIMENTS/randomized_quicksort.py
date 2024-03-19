import random

def r_partition(array, low, high):
    pivot = random.choice(array)

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

def r_quickSort(array, low, high):
    r_comparisons = 0  # Initialize comparison count for this call
    if low < high:
        pi = r_partition(array, low, high)
        r_comparisons += high - low  # Count comparisons made in this call
        r_comparisons += r_quickSort(array, low, pi - 1)  # Recursively sort left partition
        r_comparisons += r_quickSort(array, pi + 1, high)  # Recursively sort right partition
    return r_comparisons

def quickSort(array, low, high):
    comparisons = 0  # Initialize comparison count for this call
    if low < high:
        pi = partition(array, low, high)
        comparisons += high - low  # Count comparisons made in this call
        comparisons += quickSort(array, low, pi - 1)  # Recursively sort left partition
        comparisons += quickSort(array, pi + 1, high)  # Recursively sort right partition
    return comparisons

data = [i for i in range(1,5)]
print("Unsorted Array")
print(data)

size = len(data)
total_comparisons = quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
print(f"total comparisons with last pivot = {total_comparisons}")
print("-----------------------")

data = [i for i in range(1,5)]
print("Unsorted Array")
print(data)

size = len(data)
total_r_comparisons = r_quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

print(f"total comparisons with random pivot = {total_r_comparisons}")
