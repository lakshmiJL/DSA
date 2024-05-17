# Linear Search
arr = list(map(int, input("Enter the numbers - ").split()))
key = int(input())

if key in arr:
  print("Key Exist")

# Method - 1
for i in range(0, len(arr)):
  if arr[i] == key:
    print("Key Exist")

# Method - 2
for num in arr:
  if num == key:
    print("Key Exist")


#Time Complexity of the above Algorithm is O(n).

# Binary Search
# Time Complexity  - O(logn)
# Condition - The array elements should always be sorted

# Method - 1 Recursive
def binary_search(arr, low, high, key):
  mid = (low + high)//2
  if low <= high:
    if arr[mid] == key:
      return mid
    elif arr[mid] < key:
      return binary_search(arr, mid+1, high, key)
    else:
      return binary_search(arr, low, mid-1, key)
  else:
    return -1

print(binary_search([1,2,3,4,5], 0, 4, 9))

# Method - 2 Iterative
arr = list(map(int, input("Enter the numbers - ").split()))
key = int(input())

start = 0
end = len(arr)-1

flag = False

while start <= end:
  mid = (start + end)//2

  if arr[mid] == key:
    print("Key Found")
    flag = True
    break
  elif arr[mid] > key:
    end = mid - 1
  else:
    start = mid + 1

if flag == False:
  print("No Key Found")