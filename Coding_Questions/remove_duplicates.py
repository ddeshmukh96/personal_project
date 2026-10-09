"""
Write a code to remove duplicates from a list without
built-it function
"""

l=[5,4,9,2,1,4,7,6,2,4,5]

def rm_dup(l):
    unique_list=list(set(l))
    print(unique_list)

# rm_dup(l)

def dup_rm(l):
    unq_list=[]
    for num in l:
        if num not in unq_list:
            unq_list.append(num)
    return unq_list

# print(dup_rm(l))

def remove_duplicates(l):
    unq_list=[]
    for num in l:
        dup=False
        for item in unq_list:
            if num==item:
                dup=True
                break
        if dup==False:
            unq_list=unq_list+[num]
    return unq_list

print(remove_duplicates(l))