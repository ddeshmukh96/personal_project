"""
Write a program to return array where each element is a product of
all other elements (no division).
"""
arr=[1,2,3,4]

arr_dup=[5,8,4,5,3,2,3]

# Way 1: Brute Force approach O(n2). Works for all cases

def arr_prod(arr):
    n=len(arr)
    res=[]
    for i in range(n):
        product=1
        for j in range(n):
            if i==j:
                continue
            product=product*arr[j]
        res.append(product)
    return res

# print(arr_prod(arr))
# print(arr_prod(arr_dup))

# Way 2 : Divison O(n). All cases can be handled

def array_prod(arr):
    res=[]
    prod=1
    zero_count=0
    for num in arr:
        if num==0:
            zero_count+=1
            continue
        prod=prod*num
    
    if zero_count>1:
        return [0]*n
    
    if zero_count==1:
        for num in arr:
            if num==0:
                res.append(prod)
            else:
                res.append(0)
        return res
    
    for num in arr:
        res.append(prod//num)
    
    return res

print(array_prod(arr))
print(array_prod([4,5,9,7,2,7,3,4,1]))

# Way 3: Prefix and suffix O(n). Could be used for all cases

def array_product(arr):
    n=len(arr)
    res=[1]*n
    prefix_prod=1
    for i in range(n):
        res[i]=res[i]*prefix_prod
        prefix_prod=prefix_prod*arr[i]
    suffix_prod=1
    for j in range(n-1,-1,-1):
        res[j]=res[j]*suffix_prod
        suffix_prod=suffix_prod*arr[j]
    return res

# print(array_product(arr))
# print(array_product([4,5,9,7,2,7,3,4,1]))

# print(array_prod([4,5,9,7,2,7,3,4,1]))

# print(array_product([4,5,9,7,0,7,0,4,1]))

# print(arr_prod([4,5,9,7,0,7,8,4,1]))