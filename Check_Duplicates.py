#Given a list find if duplicate elements are present or not
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

My_Lst=[1, 10, 2, 6, 5, 3]
def find_max(ans):
    current_max=0
    for i in ans:
        if i>current_max:
            current_max=i
    return current_max
def largest_product(ans):
    Prd_of_elements=[]
    for i in range(len(ans)):
        current_product=0
        for j in range(i+1,len(ans)):
            current_product=i*j
        Prd_of_elements.append(current_product)
    return find_max(Prd_of_elements)

print(largest_product(My_Lst))