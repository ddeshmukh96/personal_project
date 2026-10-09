"""
Write a program to find subarray having max sum in a array.

"""

arr=[-2,1,-3,4,-1,2,1,-5,4]

#1 : Brute force approach

def max_subarr(arr):
    n=len(arr)
    max_sum=float('-inf')
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum=curr_sum+arr[j]
            max_sum=max(max_sum,curr_sum)
    return max_sum

# print(max_subarr(arr))
# print(max_subarr([5,4,-1,7,8]))
# print(max_subarr([-3,-2,-5]))

#2 : Kdane's Algorithm

def subarr_max(arr):
    n=len(arr)
    max_sum=float('-inf')
    curr_sum=0
    for i in range(n):
        curr_sum=max(curr_sum+arr[i],arr[i])
        max_sum=max(max_sum,curr_sum)
    return max_sum

# print(subarr_max(arr))
# print(subarr_max([5,4,-1,7,8]))
# print(subarr_max([-3,-2,-5]))