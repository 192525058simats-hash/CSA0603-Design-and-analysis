arr = [1, 2, 2, 4, 4]

count = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            if (i + 1) % (j + 1) == 0 or (j + 1) % (i + 1) == 0:
                count += 1

print("Count:", count)

# Time Complexity: O(n^2)
# Space Complexity: O(1)