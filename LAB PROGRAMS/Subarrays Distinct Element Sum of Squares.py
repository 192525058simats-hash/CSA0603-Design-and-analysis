arr = [1,2,1]
total=0
for i in range(len(arr)):
    distinct=set()
    for j in range(i,len(arr)):
        distinct.add(arr[j])
        total+=len(distinct)**2
print("sum of squares ",total)
# Time Complexity: O(n^2)
# Space Complexity: O(n)