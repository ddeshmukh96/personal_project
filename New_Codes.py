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
    resulting_List1=[]
    if n%2==0:
        for i in range(0,(n//2)):
            j=n-1-i
            New_sum=G[i]+G[j]
            resulting_List1.append(New_sum)
        Final_sum=sum(resulting_List1)
        # print(Final_sum)
        return Final_sum
    else:
        for i in range(0,(n//2)+1):
            j=n-1-i
            if i!=j:
                New_sum=G[i]+G[j]
                resulting_List1.append(New_sum)
            else:
                New_sum=G[i]
                resulting_List1.append(New_sum)
        Final_sum=sum(resulting_List1)
        return Final_sum

# print(pallindrome_sum(G))


matrix_1=[[1,0,0,1],
          [0,1,0,1],
          [1,0,1,0],
          [0,1,1,0]]
#Calculate the count of 1
def count_of_element(matrix_1):
    count_of_1=0
    for i in range(0,len(matrix_1)):
        for j in range(0,len(matrix_1)):
            if matrix_1[i][j]==1:
                count_of_1=count_of_1+1
    return count_of_1

# print(count_of_element(matrix_1))

"""
Given a dungeon 1 is a wall and 0 is a ground
Find the number of safe groung cells

A cell is considered safe if it is surrounded by walls on all four side

Suppose a cell is on i j so its up down Lh side and RH side should be walls


"""

dungeon_matrix=[[1,0,0,1,0],
                [0,1,0,1,1],
                [1,0,1,0,1],
                [0,1,0,1,0],
                [1,0,1,0,1]]
"""
          0 1 2 3 4
dungeon=[[1,0,0,1,0], 0
         [0,1,0,1,1], 1
         [1,0,1,0,1], 2
         [0,1,0,1,0], 3
         [1,0,1,0,1]] 4

         d[2][1]
       t d[1][1]  -1 i=2
       b d[3][1]  +1 i=2
       l d[2][0]  -1 i=2
       r d[2][2]  +1
"""
def dungeon(dungeon_matrix):
    safe_cell_count=0
    for i in range(1,len(dungeon_matrix)-1):
        for j in range(1,len(dungeon_matrix)-1):
            if dungeon_matrix[i][j]==0:
                if dungeon_matrix[i-1][j]==1 and dungeon_matrix[i+1][j] and dungeon_matrix[i][j-1] and dungeon_matrix[i][j+1]:
                    safe_cell_count=safe_cell_count+1
    return safe_cell_count

# print(dungeon(dungeon_matrix))


#Peak findings ()
list3=[1,7,3,2,5,8,7,1]
def finding_peaks(list3):
    peak_count=0
    for i in range(1,len(list3)-1):
        if list3[i]>list3[i+1] and list3[i]>list3[i-1]:
            peak_count=peak_count+1
    return peak_count

# print(finding_peaks(list3))

"""
       0 1 2 3 4 5 6 7
stock=[3,7,1,2,5,8,7,1]
   i            j
buy day     sell day       profit
 0              1             4         j=i+1
 0              2            -2         j=0+2
 0              3            -1
 0              4             2
 0              5             5
 0              6             4
 0              7            -2
 1              2            -6       
 1              3            -5
 1              4            -2
 1              5             1
 1              6             0
 1              7            -6
 2              3             1
 2              4             4
 2              5             7
 2              6             6
 2              7             0
 3              4             3
 3              5             6
 3              6             5
 3              7            -1
 4              5             3
 4              6             2
 4              7            -4
 5              6            -1
 5              7            -7
 6              7            -6


"""

#      0 1 2 3 4 5 6 7
stock=[3,7,1,2,5,8,7,1]
s2=[7,6,5,4,3,2,1]
def max_profit(stock):
    Total_profit=0
    opr_count=0
    for i in range(0,len(stock)-1):
        for j in range(i+1,len(stock)):
            opr_count=opr_count+1
            if stock[i]<stock[j]:
                current_profit=stock[j]-stock[i]
                if current_profit>Total_profit:
                    Total_profit=current_profit
    # print(opr_count)
    return Total_profit
# print(max_profit(s2))

def total_profit(stock):
    present_profit=0
    min_buy_price=stock[0]
    for i in range(1,len(stock)):
            daily_profit=stock[i]-min_buy_price
            if min_buy_price<stock[i]:
                min_buy_price=stock[i]
            if daily_profit>present_profit:
                present_profit=daily_profit
    return present_profit

print(total_profit(s2))

