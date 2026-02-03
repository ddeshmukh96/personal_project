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
