import re

with open('example.txt', 'r') as file:
    content = file.read()
    # print(content)

lines = content.split()
first = 0
last = 0
count = 0

def word_to_num(word):
    word_to_num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                        "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
    return word_to_num_dict.get(word, word)

for i in lines:
    for j in range(len(i)):
        if i[j].isdigit():
            first = i[j]
            break
        word = re.findall(r'one|two|three|four|five|six|seven|eight|nine|zero', i[-j:5-j])
        first = word_to_num(word)
    for k in range(len(i)):
        if i[-k-1].isdigit():
            last = i[-k-1]
            break
        word = re.findall(r'one|two|three|four|five|six|seven|eight|nine|zero', i[-j:5-j])
        second = word_to_num(word)
    # print(first + last)
    count += int(first + last)

print(count)
