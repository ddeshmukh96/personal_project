# Write a program to 

L=[1,2,1,3,4,5,8,7,8,7]
def compute_squares(L):
    result=[]
    for i in L:
        sq=i*i
        result.append(sq)
    return result

print(compute_squares(L))
