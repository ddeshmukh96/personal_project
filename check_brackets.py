from stack import stack,push,delete,get_top
"""
((()))()()
((())()()
)()
(
()()
)(
) - closed
( - open
Given a string check it is well formed or not

( ( ( ) ) ) ( ) ( )
0 1 2 3 4 5 6 7 8 9

( ( ( ) ) ( ) ( )
0 1 2 3 4 5 6 7 8

) (    no condition like top=(
0 1

(
0

( ) ( )
0 1 2 3

( ( ) ( ) ) )
0 1 2 3 4 5 6

empty_stack=[]

"""
s="("
def check_well_formed():
    for i in s:
        if i=='(':
            push('(')
        if i==')':
            x=get_top()
            if get_top()==None:
                return False
            else:
                delete()
    if get_top()!=None:
        return False
    return True

# print(check_well_formed())        

"""
s1={[[()]]}[[]]()

s2=[}

s3=][

s4=()()[[[)]]

"""