# Bubble sort implementation to sort
# elements in descending order.
 
def print1(a, n):
 
    for i in range(0,n+1):
        print(a[i],end=" ")
    print("")
 
 
# Sorts a[] in descending order using
# bubble sort.
def sort(a, n):
 
    for i in range(n,0,-1):
        for j in range(n, n - i,-1):
            if (a[j] > a[j - 1]):
                a[j], a[j-1]=a[j-1], a[j]
    print1(a,n)
 
 
# Driver code
n = 7
a = [2,4,3,2,4,5,3]
 
sort(a, n-1)


def InsertionSort(a):
  
    # traversing the array from 1 to length of array(a)
    for i in range(1, len(a)):
  
        temp = a[i]
  
        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp > a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp
  
a = [10, 5, 13, 8, 2]
InsertionSort(a)
print("Array after sorting:")
print(a)