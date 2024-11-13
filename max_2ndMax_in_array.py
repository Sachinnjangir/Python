def max(arr):
    max=arr[0]
    for x in arr:
        if x>max:
            max = x
    return max
arr=[2,3,5,9,7,55]
print("max of array:",max(arr))


def max(arr):
    max=arr[0]
    secmax=arr[0]
    for x in arr:
        if x>max:
            secmax=max
            max = x
        elif x> secmax and x!=max:
            secmax=x
    return secmax

arr=[2,3,5,9,7,55]
print("max of array:",max(arr))


# Method 3: By traversing the entire list
arr = [543, 321, 643, 34, 523]

def Method3(arr):  
    SL_Val = arr[0]  
    L_Val = arr[0]  
    for i in range(len(arr)):  
        if arr[i] > L_Val:  
            L_Val = arr[i]  
  
    for i in range(len(arr)):  
        if arr[i] > SL_Val and arr[i] != L_Val:
            SL_Val = arr[i]
  
    return SL_Val
    
x = Method3(arr)
print("The second largest element in the list is", x)


# Method 2: Sort the list in ascending order and print the second last element in the list.
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
 
# Removing duplicates from the list
list2 = list(set(list1))
 
# Sorting the  list
list2.sort()
 
# Printing the second last element
print("Second largest element is:", list2[-2])


#Method 3: By removing the max element from the list
list1 = [10, 20, 4, 45, 99]
 
# new_list is a set of list1
new_list = set(list1)
 
# Removing the largest element from temp list
new_list.remove(max(new_list))
 
# Elements in original list are not changed
# print(list1)
print(max(new_list))


y=[12,34,45,9,8,90,3,1,7,6]
y=sorted(y)
print(y)
z= y[1:7:2]
x=y[0:7:2]
print(z+x)
#list2 = list(set(y))
#print(list2)