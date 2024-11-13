#List 
a=["apple","mang","cherry"]
a[1]
#replace item value
a[2]="bana"
a.append(2)
a.insert(3,"sachin")
a.remove(2)
a.pop()
a.pop(1)

#TUPLES
x=(21,36,14,25,"sakshi","sachin",21,23,21)
x.count(21)
x.index(1)
y= list(x)
y[1]= "apple"
x= tuple(y)
y
#unpacking tuple
f=("apple","banana","mango")
(red,yellow,green)= f
print(red)

#SET
 s={21,25,56,87,96,20}
 s.remove(25)
 s.pop()
 S= {"a","b",2}
 s.update(S)
 
 #Dictionary
 dict1={1:"sac",2:"saks",5:"tt"}
 dict1[2]
 dict1.keys()
 dict1.values()
 dict1.get(1)
 keys = ["Name","class","love"]
 values = ["Sachin","mca","sakshi"]
dict1["last"]="jangir"
dict1  
del dict1["love"]
dict1.get(3)
prog = {'js':'atom','python':['jupyter','anaconda'],'java':{'jse','jee'}}
prog["js"]
prog["python"]
prog["python"][0]
prog["java"]["jee"]
dict1={1:"sac",2:"saks",5:"tt"}
dict1[1]= 'sachin
dict1['last']='jangir'
dict1.pop['last']
print(dict1)

#import math (use of maths function)
import math
q= math.sqrt(25)
q
print(math.floor(36.8))
print(math.ceil(36.1))
print(math.pow(3,2))
print(math.pi)
print(math.factorial(5))
from math import pow,pi,sqrt


