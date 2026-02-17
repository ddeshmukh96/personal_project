"""
[13,12]

Start with an empty stack perform following operation

push x
pop
top
print

with every stack we need a top


[3,2,5]  top=2
[3,2]  top=1
[3]    top=0
[]     top=-1
"""
stack=[]
top=-1
# num_opps=10
def push(x):
    global top
    top=top+1
    stack.append(x)
    # return stack

def delete():
    global top
    if top!=-1:
        top=top-1
        stack.pop()
        # return stack

def get_top():
    global top
    if top!=-1:
        return stack[top]
    return None
    
# print(push(5))
# print(push(3))
# print(push(2))
# print(delete())
# print(get_top())
# print(stack)