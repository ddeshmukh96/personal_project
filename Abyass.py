
calls=0

def fibonacci(n):
    global calls
    calls+=1
    # Write your code here.
    if n==0:
        return 0
    if n==1:
        return 1
    fn=fibonacci(n-1)+fibonacci(n-2)
    return fn
        

n = int(input())
print(fibonacci(n))
print(calls)
"""
                                  f(5)
                           /              \
                        f(4)              f(3)
                       /   \              /   \
                    f(3)   f(2)       f(2)   f(1)
                   / \     /   \      /   \
                f(2) f(1) f(1) f(0) f(1)  f(0)
                /  \
              f(1) f(0)

"""