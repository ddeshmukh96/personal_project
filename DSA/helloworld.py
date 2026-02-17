def checkifNumExist(L,x):
    for n in L:
        if(n==x):
            return True
    return False

L=[1,2,1,3,4,5,8,7,8,7]
k=int(input("Give the number: "))
def check_count(L):
    x=0
    for i in range(0,len(L)):
        if k==L[i]:
            x=x+1
    return x

print(check_count(L))