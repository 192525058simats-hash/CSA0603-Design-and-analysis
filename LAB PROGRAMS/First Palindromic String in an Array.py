arr=['hello','world','level','python','noon']
for word in arr:
    if word == word[::-1]:
        print(word)
        break
else:
    print("no palindrome string")
# Time Complexity: O(n * m)
# n = number of strings, m = length of string 