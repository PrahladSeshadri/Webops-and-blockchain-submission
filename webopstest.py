import array as arr
def flatten(a):
    x=arr.array('i', [])
    for i in a:
        if type(i) == list: #type of array in python is list (afaik)
            x.extend(flatten(i)) #reducing the dimensionality of the array each time function is called, and finally extending when list becomes !D
        else:
            x.append(i) #appending integer
    return x
a=[1, [2, [3, [4, 5]], 6], 7]
x=flatten(a)
print(x.tolist())
                     
