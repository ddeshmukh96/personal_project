"""
Write a program to reverse a given number

"""

num=int(input("Enter the number to be reversed: "))

def reverse_number(num):
    rev_num=''
    for i in range(len(str(num))-1,-1,-1):
        rev_num=rev_num+str(num)[i]
    return int(rev_num)

print(reverse_number(num))


def number_reverse(num):
    rev_num=0
    while num>0:
        digit=num%10
        rev_num=rev_num*10+digit
        num=num//10
    return rev_num

print(number_reverse(num))

print(str(num)[::-1])