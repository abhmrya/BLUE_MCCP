from functools import reduce

ls1 = [1,2,3,4,5,6,7,8,9,10]

def myfun(a):
    if a%2==0:
        print(a)
        return a

def myfunn(a,b):
    if a%2==0:
        print(a)
    return a+b

print(list(map(myfun,ls1)))

print(list(filter(myfun,ls1)))

print(reduce(myfunn,ls1))