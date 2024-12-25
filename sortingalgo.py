#slection sort

arr = [13, 46, 24, 52, 20, 9]
i = 0
j = len(arr) - 1
while i < j:
    minimum = i
    for k in range(i, j + 1):
        if arr[k] < arr[minimum]:
            minimum = k
    arr[minimum], arr[i] = arr[i], arr[minimum]
    i += 1

print(arr)

#bubble sort

arr = [13, 46, 24, 52, 20, 9]
i = 0
j = len(arr) - 1
while i < j:
    for k in range(i, j):
        if arr[k] > arr[k + 1]:
            arr[k], arr[k + 1] = arr[k + 1], arr[k]

    j -= 1

print(arr)

# insersion sort

arr = [13, 46, 24, 52, 20, 9]

for i in range(len(arr)):
    j = i
    while j > 0 and arr[j - 1] > arr[j]:
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1
print(arr)

# merge sort
arr = [13, 46, 24, 52, 20, 9]


def mergeSort(arr, low, high):
    def merge(arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        while (left <= mid) and (right <= high):
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    if low >= high: return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)
    return arr


print(mergeSort(arr, 0, 5))

#quick sort
arr = [13, 46, 24, 52, 20, 9]


def quickSort(arr, low, high):
    def swapper(arr, low, high):
        pivot = low
        i = low
        j = high
        while i < j:
            while arr[pivot] >= arr[i] and i < high:
                i += 1
            while arr[pivot] < arr[j] and j > low:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[pivot], arr[j] = arr[j], arr[pivot]

        return j

    if low < high:
        pivot = swapper(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

    return arr


print(quickSort(arr, 0, 5))

#Recursive Bubble Sort
arr = [13, 46, 24, 52, 20, 9]


def rBubble(arr, n):
    if n == 0:
        return
    for i in range(n):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    rBubble(arr, n - 1)
    return arr


print(rBubble(arr, 5))

#Recursive Insertion Sort

arr = [13, 46, 24, 52, 20, 9]


def rInsertion(arr, n):
    if n >= len(arr):
        return
    while n > 0 and arr[n - 1] > arr[n]:
        arr[n - 1], arr[n] = arr[n], arr[n - 1]
        n -= 1

    rInsertion(arr, n + 1)
    return arr

print(rInsertion(arr,0))

