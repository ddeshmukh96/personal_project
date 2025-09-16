#Add 2 list
L1=[1,5,8,9,5,7]
L2=[2,7,6,3,6,8]

#L3=[3,12,14,12]
def adding_list(L1,L2):
    count_self=0
    L3=[]
    for i in range(0,len(L1)):
        for j in range(0,len(L2)):
            count_self=count_self+1
            if i==j:
                print("<<< i and j are same: ",i,j)
                addup=L1[i]+L2[j]
                L3.append(addup)
            else:
                print("XXX i and j are not same: ",i,j)
    print(count_self)
    return L3

# print(adding_list(L1,L2))

def adding_list(L1,L2):
    count_self=0
    L3=[]
    for i in range(0,len(L1)):
        addup=L1[i]+L2[i]
        count_self+=1
        L3.append(addup)
    print(count_self)
    return L3

# print(adding_list(L1,L2))

#MATRIX
A=[ [1,2,3],
    [4,5,6],
    [7,8,9]]
# print(A)
# for i in range(0,3):
#     for j in range(0,3):
#         print(A[i][j],end=" ")
#     print("\n")
B=[ [9,8,7],
    [6,5,4],
    [3,2,1]]

C=[ [0,0,0],
    [0,0,0],
    [0,0,0]]

"""
     0 1 2
   0 1 2 3
   1 4 5 6
   2 7 8 9

C=[ [10 10 10],
    [10 10 10],
    [10 10 10]]

"""
def sum_of_matrix(A,B):
    for i in range(0,3):
        for j in range(0,3):
            C[i][j] = A[i][j] + B[i][j]
    return C
x=sum_of_matrix(A,B)
# for i in range(0,3):
#     for j in range(0,3):
#     #     print(C[i][j],end=" ")
#     # print("\n")

# print(x)


#Given a list print the list in reverse
#       0 1 2 3 4
List_R=[3,5,7,8,9]
def reverse_list(List_R):
    List_new=[]
    for i in range((len(List_R)-1),-1,-1):
        List_new.append(List_R[i])
    return List_new
# print(reverse_list(List_R))

#pallindrome sum

"""
0 4  i+j = n-1
3+9

1 3
5+8

2 2   
7 7

"""
G=[3,5,7,8,9]
n=len(G)
def pallindrome_sum(G):
    New_List1=[]
    if n%2==0:
        for i in range(0,(n//2)):
            j=n-1-i
            New_sum=G[i]+G[j]
            New_List1.append(New_sum)
            Final_sum=sum(New_List1)
        return Final_sum
    else:
        for i in range(0,(n//2)+1):
            j=n-1-i
            if i!=j:
                New_sum=G[i]+G[j]
                New_List1.append(New_sum)
            else:
                New_sum=G[i]
                New_List1.append(New_sum)
            Final_sum=sum(New_List1)
        return Final_sum

print(pallindrome_sum(G))