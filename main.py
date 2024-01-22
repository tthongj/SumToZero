import numpy as np

def mergesort(arr):
    n = len(arr)
    merge = []

    arr.sort()

    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                merge.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return merge

# Example usage:
L = np.random.randint(-10**6, 10**6, size=np.random.randint(3, 3001))
result = mergesort(L)
print(result)
