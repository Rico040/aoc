import re

with open('example.txt', 'r') as file:
    content = file.read()
    # print(content)

lines = content.split()
first = 0
last = 0
count = 0

for i in lines:
    matches = re.findall(r'[a-zA-Z]')
    print(matches)
    count += int(first + last)

print(count)
