"""
Write a program to find the index of 2 elements in the list such that
the sum of those 2 elements is equal to the given target value
"""

l=[1,5,9,7,3,4,8]

target=12

# Way 1: Brute Force Method

def two_sum_brute(l, target):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == target:
                return [i, j]

# Way 2 : Hash Map / Dictionary Method

def two_sum(l,target):
    dict_map={}
    
    for num in range(len(l)):
        comp=target-l[num]
        
        if comp in dict_map:
            return [dict_map[comp],num]
    
        dict_map[l[num]]=num

print(two_sum(l,target))
print(two_sum_brute([3,11,17,9,7,6],10))
# print(two_sum([3,3],6))