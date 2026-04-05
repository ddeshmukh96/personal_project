# Given a list find if duplicate elements are present or not
# 1 st Method
G=[1,5,3,5]
def dup_elements(Lst):
    found_dup=False
    for i in range(len(Lst)):
        for j in range(i+1,len(Lst)):
            print(Lst[i],Lst[j])
            if Lst[i]==Lst[j]:
                print(Lst[i]==Lst[j])
                found_dup=True
    return found_dup
# print(dup_elements(G))

# 2nd Method
G=[1,5,3,5]
def dup_elements(Lst):
    for i in range(len(Lst)):
        for j in range(i+1,len(Lst)):
            print(i,j)
            if Lst[i]==Lst[j]:
                return True
    return False
    
# print(dup_elements(G))

# Write a code to find the Largest of product of elements in a list
# Method 1
My_Lst=[1, 10, 2, 6, 5, 3]
def find_max(Lst):
    current_max=0
    for i in Lst:
        if i>current_max:
            current_max=i
    return current_max
# print(find_max(My_Lst))
def largest_product(Lst):
    Prd_of_elements=[]
    for i in range(len(Lst)):
        for j in range(i+1,len(Lst)):
            # print(Lst[i],Lst[j])
            # print(current_product)
            current_product=Lst[i]*Lst[j]
            # print(current_product)
            Prd_of_elements.append(current_product)
    print(Prd_of_elements)
    return find_max(Prd_of_elements)

# print(largest_product(My_Lst))

# Method 2
def largest_product(Lst):
    Productis=0
    for i in range(len(Lst)):
        for j in range(i+1,len(Lst)):
            # print(Lst[i],Lst[j])
            # print(current_product)
            current_product=Lst[i]*Lst[j]
            # print(current_product)
            if Productis < current_product:
                Productis=current_product
    return Productis

# print(largest_product(My_Lst))


# Print pairs function
listA=[3,5,7,8,1]
"""
n-1 + n-2 + n-3 + ......1

"""
def print_pairs_sum(listA):
    for i in range(0,len(listA)):
        for j in range(i+1,len(listA)):
            x=listA[i]+listA[j]
            print(x)
# print_pairs_sum(listA)

# Print difference of sum of even indices and odd indices
listB=[1,2,3,4,5,6,7,8]
def difference_even_odd(listB):
    Even_number=0
    Odd_number=0
    for i in range(0,len(listB)):
        if i%2==0:
            Even_number=Even_number+listB[i]
        else:
            Odd_number=Odd_number+listB[i]
    return Even_number-Odd_number
# print(difference_even_odd(listB))


"""
listC=[3,7,1,2,1,1,1,3,5,5,7,2,2,9]

           0 1 2 3 4 5 6 7 8 9 10.......................100
frequency=[0,4,3,2,0,2,0,2,0,1,0,0,0,0,0................,0]
           
           0 1 2 3 4 5 6 7 8 9
frequence=[0,4,3,2,0,2,0,2,0,1]

"""

# Compute frequency of elements and put them in a list having 10 elements
"""This Algorithm runs in order n x n i.e. n2 (n square)"""
import random
listC=[]
for _ in range(100_000):  # 1 lakh = 100,000
    num = random.randint(1, 1000000)  # You can adjust the range as needed
    listC.append(num)

def compute_fequency_A1(listC):
    initial_list=[]
    for i in range(0,100_000):
        initial_list.append(0)
        initial_count=0
        for j in range(0,len(listC)):
            if listC[j]==i:
                initial_count=initial_count+1
        initial_list[i]=initial_count
    return initial_list

# print(compute_fequency_A1(listC))

"""This Algorithm runs in order n only"""
def compute_fequencyA2(listC):
    frequency_array=[]
    for i in range(0,1000005):
        frequency_array.append(0)
    for j in listC:
        frequency_array[j]=frequency_array[j]+1

    return frequency_array

print(compute_fequencyA2(listC))

