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
print(dup_elements(G))

# 2nd Method
G=[1,5,3,5]
def dup_elements(Lst):
    for i in range(len(Lst)):
        for j in range(i+1,len(Lst)):
            print(i,j)
            if Lst[i]==Lst[j]:
                return True
    return False
    
print(dup_elements(G))

# Write a code to find the Largest of product of elements in a list
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
        current_product=0
        for j in range(i+1,len(Lst)):
            # print(Lst[i],Lst[j])
            # print(current_product)
            current_product=Lst[i]*Lst[j]
            # print(current_product)
            Prd_of_elements.append(current_product)
    # print(Prd_of_elements)
    return find_max(Prd_of_elements)

print(largest_product(My_Lst))