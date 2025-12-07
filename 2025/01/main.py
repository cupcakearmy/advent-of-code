def calc_1(lines):
    position = 50
    countZero = 0
    for line in lines:
        left = line[0] == "L"
        distance = int(line[1:])
        if left:
            distance *= -1
        position = (position + distance) % 100
        if position == 0:
            countZero += 1
    return countZero


# PART 2


def calc_2(lines):
    position = 50
    countZero = 0
    for line in lines:
        left = line[0] == "L"
        distance = int(line[1:])
        rounds = abs(distance) // 100
        countZero += rounds
        distance = distance % 100
        if left:
            distance *= -1
        distanceToZero = position if left else 100 - position
        passesZero = abs(distance) >= distanceToZero
        if passesZero and position != 0:
            countZero += 1
        position = (position + distance) % 100
    return countZero


def parse(raw: str):
    return f.read().strip().splitlines()


with open("./2025/01/train.txt") as f:
    d = parse(f)
    print(f"Train 1: {calc_1(d)}")
    print(f"Train 2: {calc_2(d)}")

with open("./2025/01/data.txt") as f:
    d = parse(f)
    print(f"Actual 1: {calc_1(d)}")
    print(f"Actual 2: {calc_2(d)}")
