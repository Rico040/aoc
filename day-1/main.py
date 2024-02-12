with open('input.txt', 'r') as file:
    content = file.read()
    # print(content)

lines = content.split()
first = 0
last = 0
count = 0

for i in lines:
    for j in range(len(i)):
        if i[j].isdigit():
            first = i[j]
            break
    for k in range(len(i)):
        if i[-k-1].isdigit():
            last = i[-k-1]
            break
    # print(first + last)
    count += int(first + last)

print(count)
