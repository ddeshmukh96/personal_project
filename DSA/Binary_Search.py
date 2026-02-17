
x=[-67,-45,-23,-14,-10,-8,0,2,4,5,7,12,37,48,57,98]
v=int(input("Enter the number: "))


def binary_search(x,v):
    low=0
    high=(len(x))-1
    while low<=high:
        mid=(low+high)//2
        if v==x[mid]:
            return mid
        elif v>x[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

print(binary_search(x,v))
