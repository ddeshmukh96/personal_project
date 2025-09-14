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
for i in range(0,3):
    for j in range(0,3):
        print(i,j)
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
# for i in range(0,3):
#     for j in range(0,3):
#         # print(C)

# x=sum_of_matrix(A,B)
# print(x)
