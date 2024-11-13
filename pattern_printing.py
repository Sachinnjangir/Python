# right angle pattern(Star printing )
i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1
    
# invert start pattern
i=5 
while i>=1: 
    j=1 
    while j<=i:
        print("*",end=" ") 
        j=j+1 
    print() 
    i=i-1
    
    # method 2 (right angle no. printing )
i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print()
    i=i+1
# invert no.\
i=5
while i>=1:
    j=1
    while j<=i:
        print(j,end=" ")
        j= j+1
    print()
    i=i-1
    
# meth0d 3
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j=j+1
    print()
    i=i+1

i=5
while i>=1:
    j=1
    while j<=i:
        print(i,end=" ")
        j=j+1
    print ()
    i=i-1