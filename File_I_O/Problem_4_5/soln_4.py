"""
Problem statement 4

A file contains a word "Donkey" multiple times. You need to write a program
to replace this word with ###### by updating the same file
"""


# Way 1

word="Donkey"

with open("my_text.txt","r") as f:
    content=f.read()

new_content=content.replace(word,"######")

with open("my_text.txt","w") as f:
    f.write(new_content)

"""

# Way 2

with open("my_text.txt","r") as f:
    content=f.read()
    
with open("my_text.txt","w") as f:
    f.write(content.replace("Donkey","######"))

"""
