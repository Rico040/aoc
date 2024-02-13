import re, sys

with open(sys.argv[1], 'r') as file:
    content = file.read()
    # print(content)

lines = content.split('\n')
# print(lines)

redcap, greencap, bluecap = 0, 0, 0
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
    matches = re.findall(r'\d+ \w+|;', i)
    matches.append(';')
    # print(matches)
    for j in range(len(matches)):
        check = parse_info(matches[j])
        if check:
            match check[1]:
                case "red":
                    redval += int(check[0])
                case "green":
                    greenval += int(check[0])
                case "blue":
                    blueval += int(check[0])
        else:
            if redval > redcap:
                redcap = redval
            if greenval > greencap:
                greencap = greenval
            if blueval > bluecap:
                bluecap = blueval
            redval, greenval, blueval = 0, 0, 0
    print(redcap, greencap, bluecap)
    idsum += redcap * greencap * bluecap
    redcap, greencap, bluecap = 0, 0, 0
    redval, greenval, blueval = 0, 0, 0

print(idsum)
