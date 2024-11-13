#Method -1 Using numpy

import numpy as np
x=[[1,2,3],[2,5,4],[7,8,9]]
y=[[8,5,3],[2,1,4],[4,3,5]]
result= np.array(x)+np.array(y)
print(result)

#Method 2 using nested for loop
x=[[1,2,3],[2,5,4],[7,8,9]]
y=[[8,5,3],[2,1,4],[4,3,5]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
# iterate through rows
for i in range (len(x)):
 # iterate through columns
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]

for r in result:
    print(r)