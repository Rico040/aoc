import re, sys

with open(sys.argv[1], 'r') as file:
    content = file.read()
    # print(content)

lines = content.split('\n')
# print(lines)

redcap, greencap, bluecap = 12, 13, 14
redval, greenval, blueval = 0, 0, 0
current = 0
idsum = 0

def parse_info(info):
    match = re.match(r'(\d+)\s+(\w+)', info)
    if match:
        return match.groups()
    return None

for i in lines:
    current += 1
    possible = []
    matches = re.findall(r'\d+ \w+|;', i)
    matches.append(';')
    for j in range(len(matches)):
        check = parse_info(matches[j])
        # print(check)
        if check:
            match check[1]:
                case "red":
                    redval += int(check[0])
                case "green":
                    greenval += int(check[0])
                case "blue":
                    blueval += int(check[0])
        else:
            # print(redval, greenval, blueval)
            if redval > redcap or greenval > greencap or blueval > bluecap:
                possible.append(False)
                redval, greenval, blueval = 0, 0, 0
            else:
                possible.append(True)
                redval, greenval, blueval = 0, 0, 0
    
    redval, greenval, blueval = 0, 0, 0
    if False not in possible:
        print(f"Game {current} is possible!")
        idsum += current

print(idsum)
