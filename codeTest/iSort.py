arr = [5, 88, 6, 89, 90, 87, 456, 8949, 84, 541561, 945]

for n in range(len(arr)):
    for j in range(n, 0, -1):
        if arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

print(arr)
