"""
Write a program to copy the log_file.txt to copy_log_file.txt
"""

with open("log_file.txt","r") as file:
    file_content=file.read()

with open("copy_log_file.txt","w") as f:
    f.write(file_content)