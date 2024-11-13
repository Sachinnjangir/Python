# using recursive method
def binary_search(arr,low,high,x): #x=key element i.e search element
    if high>=low:
        mid=(high+low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        else:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

arr=[2,6,9,10,15,25]
x=10
item= binary_search(arr,0,len(arr)-1,x)
if item != -1:
    print("element found at index:",str(item))
else:
    print("elment not found in array")