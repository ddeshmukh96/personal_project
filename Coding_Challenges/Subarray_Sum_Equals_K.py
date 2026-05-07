"""
Write a program to find the contiguous subarray from a given array such that summing the
elements in subarray should be equal to a value k 
"""

arr=[2, 5, 9, 7, 3, 4]
k1=19
k2=12
k3=16

# Way 1 : Brute force (Time previous_sumlexity : O(n2))

def sub_arr_sum(arr,k):
    n=len(arr)
    
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum=curr_sum+arr[j]
            if curr_sum==k:
                return arr[i:j+1]
    return "Sub-array not found"

# print(sub_arr_sum(arr,k1))
# print(sub_arr_sum(arr,k2))
# print(sub_arr_sum(arr,k3))

# Way 2 : Sliding Window Algorithm (all elements must be positive)

def sub_array_sum(arr,k):
    n=len(arr)

    curr_sum=0
    start=0

    for end in range(n):
        curr_sum = curr_sum + arr[end]

        while curr_sum > k:
            curr_sum = curr_sum - arr[start]
            start+=1
        
        if curr_sum == k:
            return arr[start:end+1]
    else:
        return "Sub-array not found"

# print(sub_array_sum(arr,k1))
# print(sub_array_sum(arr,k2))
# print(sub_array_sum(arr,k3))

# Way 3 : Hashing Algorithm (could be used for + / - elements)

def subarray_sum(arr,k):
    n=len(arr)
    
    dict_map={0:-1}
    curr_sum=0

    for i in range(n):
        curr_sum = curr_sum + arr[i]
        print(curr_sum)
        
        previous_sum = curr_sum - k
        print(previous_sum)

        if previous_sum in dict_map:
            return arr[(dict_map[previous_sum] + 1): (i+1)]
        
        dict_map[curr_sum] = i
        print(dict_map)
    
    else:
        return "Sub-array not found"

print(subarray_sum(arr,k1))
# print(subarray_sum(arr,k2))
# print(subarray_sum(arr,k3))