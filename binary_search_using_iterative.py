def binary_search(arr,x):
    low=0
    high=len(arr)-1
    mid=0
    while high>=low:
        mid=(high+low)//2
        if arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high=mid-1
        else:
            return mid
    return -1
arr= [2,5,6,8,12,20]
x=12
item=binary_search(arr,x)
if item !=-1:
    print("found at index",item)
else:
    print("Not found")
