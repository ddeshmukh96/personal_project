""" Factorial of number n """

# n=int(input("Enter no. whose factorial needs to be find"))
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

# print(factorial(n))

""" Countdown from n to 1 """

def countdown(k):
    if k==0:
        return
    print(k)
    countdown(k-1)

# countdown(8)

calls=0

"""   Fibonacci problem using recursion  """

def fibonacci(n):
    global calls
    calls+=1
    if n==0:
        return 0
    if n==1:
        return 1
    fn=fibonacci(n-1)+fibonacci(n-2)
    return fn

# n=int(input("Enter n: "))

# print(fibonacci(n))
# print(calls)


""" Fibonacci series problem using memoization

Memoization is a technique used in algorithms (especially
recursion and dynamic programming) where the results of
expensive function calls are stored so that the same
inputs are not recomputed again.

"""

def fibonacci(n,cache_list):
    global calls
    calls+=1
    # Write your code here.
    if n==0:
        return 0
    if n==1:
        return 1
    if cache_list[n]!=-1:
        return cache_list[n]
    fn=fibonacci(n-1,cache_list)+fibonacci(n-2,cache_list)
    cache_list[n]=fn
    return fn
        
n = int(input())

cache_list=[]
for i in range(0,n+1):
    cache_list.append(-1)


print(fibonacci(n,cache_list))
print(calls)

r"""
                                  f(5)
                           /              \
                        f(4)              f(3)
                       /   \              /   \
                    f(3)   f(2)       f(2)   f(1)
                   / \     /   \      /   \
                f(2) f(1) f(1) f(0) f(1)  f(0)
                /  \
              f(1) f(0)

            f(1)=1 and f(0)=0
"""
