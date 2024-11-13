
def linear_search(x,y):
    for i in range(len(x)):
        if x[i]==y:
            return i
    return -1

x=[5,4,6,9,3,4]
y=3
length=len(x)
search = linear_search(x,y)
if search==-1:
    print("not found")
else:
    print("found at index",search)