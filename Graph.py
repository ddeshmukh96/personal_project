"""
                     0 - 5
                    / \  /
                   1    3
                  /    / \
                 2    4   6


"""

g1=[
   [0,1,0,1,0,1,0],
   [1,0,1,0,0,0,0],
   [0,1,0,0,0,0,0],
   [1,0,0,0,1,1,1],
   [0,0,0,1,0,0,0],
   [1,0,0,1,0,0,0],
   [0,0,0,1,0,0,0]
]

# for i in range(0,11):
#     u=int(input("Enter the Node 1 : "))
#     v=int(input("Enter the Node 2 : "))
#     if g[u][v]==1:
#         print("Edge is Present")
#     else:
#         print("No Edge is present")

g2=[
    [1,3,5],
    [0,2],
    [1],
    [0,4,5,6],
    [3],
    [0,3],
    [3]
]

# for i in range(0,5):
#     u=int(input("Enter the Node 1 : "))
#     v=int(input("Enter the Node 2 : "))
#     found=False
#     for j in g2[u]:
#         if j==v:
#             found=True
#             print("Edge found")
#     if found==False:
#         print("Edge not found")


"""
Mistake 1

for i in range(0,5):
    u=int(input("Enter the Node 1 : "))
    v=int(input("Enter the Node 2 : "))
    found=False
    for j in g2[u]:
        if j==v:
            found=True
        print("Edge found")

In this code due to the "print("Edge found")" written in indent
of for for the every iteration it is provide the print
statement without caring the edge is found or not

"""


"""
Output format is wrong

for i in range(0,5):
    u=int(input("Enter the Node 1 : "))
    v=int(input("Enter the Node 2 : "))
    found=False
    for j in g2[u]:
        if j==v:
            found=True
            print("Edge found")
        else:
            print("Edge not found)

In this code it is iterating via loop on line 77 and printing
the answer for each node and the if found it prints the output
as "Edge Found" but the desired output was like as soon as I get
the node condition true it shoud prunt "Edge found" and finish.

"""
