# Write a program to 

L=[1,2,1,3,4,5,8,7,8,7]
def compute_squares(L):
    result=[]
    for i in L:
        sq=i*i
        result.append(sq)
    return result

print(compute_squares(L))

x=compute_squares(L)
def even_odd_count(x):
    Even_count=0
    Odd_count=0
    for n in x:
        if n%2==0:
            Even_count=Even_count+1
        else:
            Odd_count=Odd_count+1
    return Even_count, Odd_count

print(even_odd_count(x))