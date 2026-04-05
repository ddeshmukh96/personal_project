# Sliding window Algorithm
"""
Write a code to find whether A is subarray of
B and o/p is the first index
A=[3,5,2,1]
B=[7,2,3,3,3,5,2,1,6]

lst1=B
lst2=A
"""
a=[3,5,2,1]
b=[7,2,3,3,3,5,2,1,6]

# Naive Window Algorith (Brute Force)

def check_subarray(a,b):
    for i in range(len(b)):
        temp_index=i
        found=True

        for j in range(len(a)):

            if b[temp_index]!=a[j]:
                found=False
                break

            temp_index+=1
            
        if found==True:
            return (i,temp_index-1)
    else:
        return "Not found"

# print(check_subarray(a,b))

# Sliding Window Algorithm

def subarray_check(a,b):

    n,m=len(b),len(a)

    for i in range(n-m+1):

        if b[i:i+m]==a:
            return (i,i+m-1)
        
    return "Not Found"

# print(subarray_check(a,b))