#method-1
a= 5
b=10
# now we have to swap these two variable
temp = a
a=b
b=temp
print(a,b)

#Method 2
# swap 2 varaiable without 3rd variable
a,b = 5,6
a = a+b
b = a-b
a = a-b
print(a)
print(b) 

# Method =3
# with XOR(^)
a= 5
b=6
a=a^b
b=a^b
a=a^b
print(a,b)
