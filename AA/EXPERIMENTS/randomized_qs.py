import random
c1, c2 = 0, 0
def randomized_qs(arr):
    global c1
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = []
        right = []
        for i in range(len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c1 += 1
            elif arr[i] > pivot:
                right.append(arr[i])
                c1 += 1
        return randomized_qs(left) + [pivot] + randomized_qs(right)

def quicksort(arr):
    global c2
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c2 += 1
            else:
                right.append(arr[i])
                c2 += 1
        return quicksort(left) + [pivot] + quicksort(right)

arr = [i for i in range(400)]

print('Normal Quicksort')
print("Sorted Array:", quicksort(arr))
print("Number of Comparisons:", c2)

print("Randomized QS")
print("Sorted Array:", randomized_qs(arr))
print("Number of Comparisons:", c1)