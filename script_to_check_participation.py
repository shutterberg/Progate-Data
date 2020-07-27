import re

python = 0
java = 0
both = 0
count = 0

with open('progate.txt') as file:
    lines = file.readlines()
    for line in lines:
        count += 1
        result = re.findall(r'(\d+) %',line)
        if result[0]=='100':
            java += 1
        if result[1]=='100':
            python += 1
        if result[0]=='100' and result[1]=='100':
            both += 1
            
print("Total No of learners:",count)
print("Java",java)
print("Python",python)
print("Both",both)
