arr=[3,6,5,4,9,77,43,76]

def hash_fun(x,size):
    return x % size

# for v in arr:
    print(hash_fun(v,arr))

hash_table=[]

def build_hash_table(hash_table,arr):
    for p in range(0,len(arr)):
        hash_table.append([])

    for v in arr:
        hash_index=hash_fun(v,len(arr))
        hash_table[hash_index].append(v)


build_hash_table(hash_table,arr)
# print(hash_table)

def search(hash_table,var):
    var_lst_index=hash_fun(var,len(hash_table))
    for num in hash_table[var_lst_index]:
        if num==var:
            print("Yes")
            return
    print("No")


def insert_num(hash_table,var):
    var_lst_index=hash_fun(var,len(hash_table))
    hash_table[var_lst_index].append(var)

# for i in range(0,5):
#     var=int(input("Enter var to search: "))
#     search(hash_table,var)
#     # insert_num(hash_table,var)

def delete(hash_table,var):
    var_lst_index=hash_fun(var,len(hash_table))
    for num in hash_table[var_lst_index]:
        if num==var:
            hash_table[var_lst_index].remove(var)

val_del=int(input("Enter num: "))
delete(hash_table,val_del)

print(hash_table)