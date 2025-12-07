def calc_1(input):
    pass


def calc_2(input):
    pass


def parse(raw: str):
    return raw


# Run
with open("./2025/XX/train.txt") as f:
    d = parse(f)
    print(f"Train 1: {calc_1(d)}")
    print(f"Train 2: {calc_2(d)}")

with open("./2025/XX/data.txt") as f:
    d = parse(f)
    print(f"Actual 1: {calc_1(d)}")
    print(f"Actual 2: {calc_2(d)}")
