

def lowerbound(key,arr):
    low,high=0,len(nums)
   
    while low < high:
        mid = (low + high)//2
        if key  <= arr[mid]:
            high = mid
        else:
            low = mid+1
    return low    
    

def upperbound(key,arr):
    low,high=0,len(nums)
    
    while low <= high:
        mid = (low + high)//2
        if key < arr[mid]:
            high = mid
        else:
            low = mid+1
    return low    
   
def bound_search(x,lst,compare):
    lo,up = 0,len(lst)
    while lo<up:
        mid = (lo+up)//2
        if compare(x,lst[mid]):
            up = mid
        else:
            lo = mid+1
    return lo

lower = lambda x, elem:x <=elem
upper = lambda x, elem:x < elem

nums =[1,2,2,3,4,4,5,6,6,7]

print(bound_search(4,nums,lower))
print(bound_search(4,nums,upper))