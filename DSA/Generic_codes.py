def countofelementsinL2(l1,l2):
    result=[]
    for i in l1:
        count_of_i=0
#        print("i is now : ",i," count of i is now : ",count_of_i)
        for j in l2:
#            print("j is now : ",j)
            if i==j:
#                print("i and j are same",i)
                count_of_i=count_of_i+1
#        print("I have counted all i's in L2 : ", count_of_i)
        result.append(count_of_i)
#        print("Result at this point is : ",result)

#    print("now returining result",result)
    return result

# print(countofelementsinL2([3,7,5,2],[3,3,7,5,1]))


l3=[1,3,7,2,0]
l4=[5,5,3,6,3,4,-1]
# k=int(input("Enter user no.: "))
def sumofcountoflistelements(l3,l4,k):
    countofelements=0
    for i in l3:
        # print("current i is : ",i)
        for j in l4:
            # print("current j is : ",j)
            if k==i+j:
                # print("Sum of i and j is = ", k)
                countofelements=countofelements+1
                # print("current count is : ",countofelements)
    # print("Final count is : ",countofelements)
    return countofelements

# print(sumofcountoflistelements(l3,l4,k))

S1="paxxap"
S2="paxyap"

def check_palindrome(S):
    for i in range(0,len(S)//2):
        j=len(S)-i-1
        if S[i]!=S[j]:
            return False
    return True

# print(check_palindrome(S1))
# print(check_palindrome(S2))
# print(check_palindrome("abddba"))
# print(check_palindrome("aba"))


def isPalindrome(string):
    if string==string[::-1]:
        return True
    return False

# print(isPalindrome(S1))
# print(isPalindrome(S2))

def checking_Palindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

print(checking_Palindrome(S1))
print(checking_Palindrome(S2))


def swapping(num1,num2):
    tempnum=num1
    num1=num2
    num2=tempnum
    return num1,num2

# x=5
# y=6
# print(swapping(x,y))

def sort_elements_in_list(Lst):
    n=len(Lst)
    for i in range(n):
        for j in range(i+1,n):
            if Lst[i]>Lst[j]:
                temp=Lst[i]
                Lst[i]=Lst[j]
                Lst[j]=temp
    return Lst

# print(sort_elements_in_list([3,5,2,1,0,10]))

