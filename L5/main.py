#Sorting - Rearrange the elements in order
#[3,1,2,5,4] = [1,2,3,4,5] / [5,4,3,2,1]

mylist = [3,1,2,5,4]
mylist.sort(reverse = True)
print(mylist)
print(mylist.sort(reverse = False))

# Bubble sort
# Time Complexity - O(n^2)

mylist = [12,34,2,5,7]

for i in range(0, len(mylist)):
  for j in range(i, len(mylist)):
    if mylist[i] < mylist[j]:
        mylist[i],mylist[j] = mylist[j], mylist[i]

print(mylist)



# Insertion Sort
# Time Complexity - O(n^2)
mylist = [12,34,2,5,7]

for i in range(0, len(mylist)):
  minElement = 10000000
  minLocation = -1
  for j in range(i, len(mylist)):
    if minElement > mylist[j]:
      minElement = mylist[j]
      minLocation = j
      mylist[i],mylist[j] = mylist[j], mylist[i]


print(mylist)

def InsertionSort(a):
  
    # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
  
        temp = a[i]
  
        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp

# array to be sorted        
a = [10, 5, 13, 8, 2]
InsertionSort(a)
print("Array after sorting:")
print(a)