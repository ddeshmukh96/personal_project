r"""
                     0 - 5
                    / \  /
                   1    3
                  /    / \
                 2    4   6

"""

"""Adjacency Matrix"""

matrix=[
   [0,1,0,1,0,1,0],
   [1,0,1,0,0,0,0],
   [0,1,0,0,0,0,0],
   [1,0,0,0,1,1,1],
   [0,0,0,1,0,0,0],
   [1,0,0,1,0,0,0],
   [0,0,0,1,0,0,0]
]

def find_edge(matrix):
    n=len(matrix)
    for _ in range(10):
        u=int(input("Enter the Node 1 : "))
        v=int(input("Enter the Node 2 : "))
        if 0<=u<n and 0<=v<n:
            if matrix[u][v]==1:
                print("Edge is Present")
            else:
                print("No Edge is present")
        else:
            print("Missing entered node number")

# find_edge(matrix)


"""Adjacency List"""
g2=[
    [1,3,5],
    [0,2],
    [1],
    [0,4,5,6],
    [3],
    [0,3],
    [3]
]

def finding_edge(g2):
    n=len(g2)
    for _ in range(0,5):
        u=int(input("Enter the Node 1 : "))
        v=int(input("Enter the Node 2 : "))
        if 0<=u<n and 0<=v<n:
            found=False
            for j in g2[u]:
                if j==v:
                    found=True
                    print("Edge found")
                    break
            if found==False:
                print("Edge not found")
        else:
            print("Invalid Nodes Entered")

# finding_edge(g2)

"""
My 1st Mistake when I wrote the code

for i in range(0,5):
    u=int(input("Enter the Node 1 : "))
    v=int(input("Enter the Node 2 : "))
    found=False
    for j in g2[u]:
        if j==v:
            found=True
    print("Edge found")

In this code due to the "print("Edge found")" written in indent
of for, for the every iteration it is provide the print
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

In this code it is iterating via loop on line 94 and printing
the answer for each node and then if found it prints the output
as "Edge Found" but the desired output was like as soon as I get
the node condition true it shoud print "Edge found" and finish.

"""


r"""
n=8 (nuber of nodes)
m=9 (number of edges)
0 1
0 3
0 2
3 4
1 5
1 2
2 5
4 5
6 7                     

                        5 — 4    6 — 7
                      / |   /
                    2 — 1  3
                     \  |  /
                        0
                                                     
"""

n=int(input("Give me number of nodes : "))
m=int(input("Give me number of edges : "))

g3=[]

# g3=[[1,2,3],[],[],[],[],[],[],[]]

for _ in range(0,n):
    g3.append([])

for _ in range(0,m):
    n1=int(input())
    n2=int(input())
    g3[n1].append(n2)
    g3[n2].append(n1)

# print(g3)

# To find the indirect edge take two inputs
n3=int(input())
n4=int(input())
visited_list=[]
for _ in range(0,n):
    visited_list.append(0)
# print(visited_list)
def walk_graph(current_node,target_node,visited_list):
    visited_list[current_node]=1
    print(visited_list)
    if current_node==target_node:
        return True
    for child in g3[current_node]:
        print(child)
        if visited_list[child]==0:
            print(visited_list[child])
            found_status=walk_graph(child,target_node,visited_list)
            if found_status==True:
                return True
    return False
        
# print(walk_graph(n3,n4,visited_list))

# To do - DFS using stack
