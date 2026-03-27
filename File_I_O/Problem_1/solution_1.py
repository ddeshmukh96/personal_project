"""
Write a program to read text from a given file 'poem.txt' and find out
 whether it contains the word "fire".
"""

# Way 1

f=open("poem.txt","r")

content=f.read()

# print(content)   # Could also use print(f.read()) to get the whole poem

if "fire" in content:
    print("got the word")
else:
    print("Didn't find the word")

f.close()


# Way 2

with open("poem.txt",'r') as f:
    content=f.read()
    if "fire" in content:
        print("got the word")
    else:
        print("Didn't find the word")   