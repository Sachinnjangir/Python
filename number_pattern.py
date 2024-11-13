# half pyramid number
n=5
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")
    
    
## 
n=5
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")
    
### reversed inverted
n=5   
for i in range(6):    
    for j in range(5-i,0,-1):    
        print(j, end=' ')    
    print("")    

###  inverted number
n= int(input("Enter the number of rows: "))    
for i in range(n,0,-1):    
    for j in range(1, i + 1):    
        print(j, end=' ')    
    print("")    