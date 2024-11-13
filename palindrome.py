# using reverse string
string=input(("Enter a letter:"))  
if(string==string[::-1]):  
      print("The letter is a palindrome")  
else:  
      print("The letter is not a palindrome")
      
 # using while loop
num=121
rev=0
x=num
while(num>0):
     dig=num % 10
     rev=(rev*10)+num % 10
     num=num//10
if x==rev:
    print('Yes, given no. is palindrome')
else:
    print("no")