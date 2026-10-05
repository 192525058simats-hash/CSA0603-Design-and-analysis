arr = [10, 25, 7, 45, 30]

maximum = arr[0]

for i in range(1, len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

print("Maximum Element:", maximum)

# Time Complexity: O(n)
# Space Complexity: O(1)