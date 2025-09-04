def checkifNumExist(L,x):
    for n in L:
        if(n==x):
            return True
    return False

x = int(input('Enter num'))
print(checkifNumExist([2,23,523,56,777],x))