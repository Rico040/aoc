import re, sys

with open(sys.argv[1], 'r') as file:
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
    matches = re.findall(r'one|two|three|four|five|six|seven|eight|nine|zero|[0-9]', i)
    if not matches[0].isdigit():
        first = word_to_num(matches[0])
    else:
        first = matches[0]
    if not matches[-1].isdigit():
        last = word_to_num(matches[-1])
    else:
        last = matches[-1]
    count += int(str(first) + str(last))


print(count)
