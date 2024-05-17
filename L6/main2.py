def merge_sort(arr):
  if len(arr) > 1:
      mid = len(arr) // 2
      left_half = arr[:mid]
      right_half = arr[mid:]
      print(left_half)
      print(right_half)
      merge_sort(left_half)
      merge_sort(right_half)
"""
      i = j = k = 0
      # Merge the two sorted halves
      while i < len(left_half) and j < len(right_half):
          if left_half[i] < right_half[j]:
              arr[k] = left_half[i]
              i += 1
          else:
              arr[k] = right_half[j]
              j += 1
          k += 1
      # Check for any remaining elements in the left half
      while i < len(left_half):
          arr[k] = left_half[i]
          i += 1
          k += 1   
      # Check for any remaining elements in the right half
      while j < len(right_half):
          arr[k] = right_half[j]
          j += 1
          k += 1
"""

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
merge_sort(my_list)
print("Sorted list:", my_list)