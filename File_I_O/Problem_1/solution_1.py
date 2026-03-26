"""
Write a program to read text from a given file 'poem.txt' and find out
 whether it contains the word "fire".
"""

f=open("poem.txt","r")

content=f.read()

# print(content)

if "fire" in content:
    print("got the word")
else:
    print("Didn't find the word")

f.close()