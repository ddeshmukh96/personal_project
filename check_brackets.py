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
s="((()))()()"
def check_well_formed(s):
    for i in s:
        if i=='(':
            push('(')
        if i==')':
            x=get_top()
            if x==None:
                return False
            else:
                delete()
    if get_top()!=None:
        return False
    return True

# print(check_well_formed(s))

"""
   0 1 2 3 4 5 6 7 8 9 10 11 12 13
s1={ [ [ ( ) ] ] } [ [  ]  ]  (  )

s2=[}

s3=][

s4=()()[[[)]]

"""

"""
   0 1  2 3 4
q=[1,25,7,8,9]
  [25 7 8 9]
  [25 7 8 9 12]

"""
s1="{[[()]]}[[]]()"
def check_well_form():
    for i in s1:
        if i=='[':
            push('[')
        elif i=='{':
            push('{')
        elif i=='(':
            push('(')
        if i==']' or i=='}' or i==")":
            x=get_top()
            if x is None:
                return False
            if x=='[' and i!=']':
                return False
            elif x=='(' and i!=')':
                return False
            elif x=='{' and i!='}':
                return False
            else:
                delete()
    if get_top() is not None:
        return False
    return True
# print(check_well_formed(s1))

s2="()()[[[)]]"
def check_well_formation(s2):
    for i in s2:
        if i=='{':
            push('{')
        elif i=='[':
            push('[')
        elif i=='(':
            push('(')
        if i=='}' or i==']' or i==')':
            top_index_value=get_top()
            if top_index_value is None:
                return False
            if top_index_value=='{' and i!='}':
                return False
            elif top_index_value=='[' and i!=']':
                return False
            elif top_index_value=='(' and i!=')':
                return False
            else:
                delete()
    if get_top() is not None:
        return False
    return True

# print(check_well_formation(s2))

s5="{()()}[{}()]"
def check_well_string_form(s5):
    for i in s5:
        if i=='{' or i=='[' or i=='(':
            push(i)
        if i=='}' or i==']' or i==')':
            top_index_value=get_top()
            if top_index_value is None:
                return False
            if i=='}' and top_index_value!='{':
                return False
            elif i==']' and top_index_value!='[':
                return False
            elif i==')' and top_index_value!='(':
                return False
            else:
                delete()
    if get_top() is not None:
        return False
    return True

print(check_well_string_form(s5))


