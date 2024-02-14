import re, sys

with open(sys.argv[1], 'r') as file:
    content = file.read()

lines = content.split('\n')
totallines = len(lines)
onelinelength = len(lines[0])

for i in range(len(lines)):
    for match in re.finditer(r'\d+', lines[i]):
        spans = match.span()
        start = spans[0]
        length = spans[1] - spans[0]
        print(spans[0], spans[1])
        for j in range(3):
            if j == 0 and i == 0:
                break
            if j == 1 and start == 0:
                if lines[start+length-1:start+length].find():
                    break
            if j == 1 and spans[1] == onelinelength:
                break
            if j == 2 and i+1 == totallines:
                break
