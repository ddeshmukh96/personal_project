lstA=[8,6,17,4,13,9,5,77,19,55]
k=int(input("Enter which largest number you want to find: "))

def largest_k(lstA,k):
    temp=lstA.copy()
    for i in range(k):
        largest=temp[0]
        print(f"for {i} the current largest number is {largest}")
        for num in temp:
            if num>largest:
                largest=num
                print(f"As num={num} is greater than largest, largest={largest}")
        if i==k-1:
            print(f"The {k}th largest number is {largest}")
            break
        temp.remove(largest)

# largest_k(lstA,k)

import heapq

def k_largest(lstA,k):

    # Creating heap list which contains k-1 elements from lstA
    heap_lst=lstA[:k]

    # Using heapq library to arrange the heap_lst so that heap_lst[0] is the smallest element
    heapq.heapify(heap_lst)

    # Iterating over the remaining list elements and perform operations
    for num in lstA[k:]:
        if num>heap_lst[0]:
            heapq.heappushpop(heap_lst,num)
    
    return f"The {k} largest number is {heap_lst[0]}"

# print(k_largest(lstA,k))
# print(k_largest([8,4,7,6,3],k))