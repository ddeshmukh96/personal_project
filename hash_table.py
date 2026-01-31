arr=[3,6,5,4,9,77,43,76]

def hash_fun(x,arr):
    return x % len(arr)

# for v in arr:
    print(hash_fun(v,arr))

hash_table=[]

def build_hash_table(hash_table,arr):
    for p in range(0,len(arr)):
        hash_table.append([])

    for v in arr:
        hash_index=hash_fun(v,arr)
        hash_table[hash_index].append(v)


build_hash_table(hash_table,arr)
print(hash_table)
