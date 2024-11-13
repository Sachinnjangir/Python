#sum of array
x=[2,5,8,7,3]
sum = 0
for element in x:
    sum+= element
print(sum)

#max & min of array
x=[25,55,84,20,10]
y=max(x)
print(y)
z= min(x)
print(z)

#avg of array elemnt
x= [25,61,2,3,4]
sum_of_element = sum(x)
total_no = len(x)
#count= 0
#for element in x:
  #  sum_of_element+=element
 #   count +=1
avg_of_array= sum(x)/count
print(avg_of_array)
average=sum_of_element/total_no
print(average)

# Count positive and negative numbers in a list

list = [-10, -21, -4, -45, 26, 93, 11]
pos,neg,zeros=0,0,0
for num in list:
    if num>=0:
        pos+=1
    elif num==0:
        zeros+=1
    else:
        neg+=1
print("positive no. in list:",pos)
print("negative no. in list:",neg)
print("Zeros no. in list:",zeros)


