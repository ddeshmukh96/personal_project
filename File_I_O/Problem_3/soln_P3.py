"""
Write a program to generate multiplication tables from 2 to 20 and
write it to the different files.Place these files in a folder for
a 13 year old student.  
"""

def table_print(n):
    
    print(f"Table of {n}")

    table=""
    
    for j in range(1,11):
        table+=f"{n} X {j} = {n*j}\n"
    
    print(table)

    with open(f"Tables/Table of {n}.txt","w") as f:
        f.write(f"Table of {n}\n\n")
        f.write(table)

start_table_with=int(input("Enter start: "))
end_table_with=int(input("Enter end: "))

if start_table_with>end_table_with:
    print("Invalid Input")
    exit()
else:
    for i in range(start_table_with,end_table_with+1):
        table_print(i)