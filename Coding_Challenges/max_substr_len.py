"""
Write a program to get the max len of sub-string in a given string
"""

s='abcabcbb'

def max_substr(s):
    n=len(s)
    max_len=0
    for i in range(n):
        my_set=set()
        for j in range(i,n):
            if s[j] in my_set:
                break
            my_set.add(s[j])
            max_len=max(max_len,(j-i+1))
    return max_len

# print(max_substr(s))
# print(max_substr('abdebabbcercchd'))

def max_of_substr(s):
    my_set=set()
    win_start=0
    max_len=0
    for win_end in range(len(s)):
        while s[win_end] in my_set:
            my_set.remove(s[win_start])
            win_start+=1
        my_set.add(s[win_end])
        max_len=max(max_len,(win_end-win_start+1))
    return max_len

print(max_of_substr('pwkewke'))
print(max_of_substr('abebabbcercchd'))


def longest_substr(s):
    n=len(s)
    max_len=0
    for i in range(n):
        my_set=set()
        for j in range(i,n):
            if s[j] in my_set:
                break
            my_set.add(s[j])
        max_len=max(max_len,len(my_set))
    return max_len

print(longest_substr(s))
print(longest_substr('pwekekw'))
print(longest_substr('abcaefg'))
print(longest_substr('tmmzuxt'))
print(longest_substr('dvdf'))
print(longest_substr('aaaaaaaaaaaaa'))
print(longest_substr('aaabaaaaegaaa'))