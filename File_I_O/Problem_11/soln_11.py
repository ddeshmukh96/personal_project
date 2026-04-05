"""
Write a program to rename a file to "renamed_by_python.txt" 
"""

import os

# os.rename('file_to_rename.txt','renamed_by_python.txt')

"""
Write a program to rename (file1.txt file2.txt file3.txt) as per user
input in one go
"""

n=int(input("Enter how many file needs to be renamed: "))

def renaming(n):
    for i in range(n):

        old_name=input(f"Enter old name of the file {i+1}: ")
        new_name=input(f"Enter new name of the file {i+1}: ")

        if os.path.exists(old_name):
            os.rename(old_name,new_name)
            print(f"{old_name} has been successfully renamed to {new_name}")
    
        else:
            print(f"{old_name} not found")

# renaming(n)