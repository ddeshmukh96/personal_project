"""
Write a program to find the line number where the word 'Python' is present
"""

# Way 1

with open("log_file.txt","r") as f:
    lines=f.readlines()

line_no=1
for line in lines:
    if 'Python' in line:
        print(f"The word 'Pthon' is present at line number: {line_no}")
        break
    line_no+=1
else:
    print("Word is not present")

# Way 2

with open("log_file.txt","r") as f:
    curr_line=1

    while True:
        line=f.readline()

        if not line:
            print("Word not found")
            break

        if "Python" in line:
            print(f"Found the word at line: {curr_line}")
            break

        curr_line+=1