def calc_1(input):
    total = 0
    for line in input:
        print(line)
        l = len(line)
        maximum = 0
        for a in range(l):
            for b in range(a + 1, l):
                x = int(line[a] + line[b])
                if x > maximum:
                    maximum = x
        print(line, maximum)
        total += maximum
    return total


def calc_2(input):
    pass


def parse(raw: str):
    return raw.read().splitlines()


# Run
with open("./2025/03/train.txt") as f:
    d = parse(f)
    print(f"Train 1: {calc_1(d)}")
    # print(f"Train 2: {calc_2(d)}")

with open("./2025/03/data.txt") as f:
    d = parse(f)
    print(f"Actual 1: {calc_1(d)}")
    # print(f"Actual 2: {calc_2(d)}")
