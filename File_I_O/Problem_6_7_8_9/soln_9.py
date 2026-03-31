"""
Write a prgram to check whether two files are identical or not

"""

with open("log_file.txt") as f:
    content1=f.read()

with open("copy_log_file.txt") as f:
    content2=f.read()

if content1==content2:
    print("Yes the files are identical")
else:
    print("Files are not identical")
