def calc_1(ids: list[tuple[int, int]]):
    invalid = 0
    for i in ids:
        for x in range(i[0], i[1] + 1):
            asStr = str(x)
            l = len(asStr)
            isEvenLength = l % 2 == 1
            if isEvenLength:
                continue
            half = l // 2
            if asStr[:half] == asStr[half:]:
                invalid += x
    return invalid


def calc_2(ids: list[tuple[int, int]]):
    invalid = 0
    for i in ids:
        for x in range(i[0], i[1] + 1):
            s = str(x)
            l = len(s)
            for m in range(1, (l // 2) + 1):
                if l % m != 0:
                    continue
                first = s[:m]
                max_multiples = l // m
                is_invalid = False
                for offset in range(1, max_multiples):
                    start = offset * m
                    end = start + m
                    if first != s[start:end]:
                        is_invalid = True
                        break
                if is_invalid:
                    continue
                invalid += x
                break
    return invalid


def parse(raw):
    ids = raw.read().strip().replace("\n", "").split(",")
    return [tuple(map(int, (i.split("-")))) for i in ids]


# Run
with open("./2025/02/train.txt") as f:
    d = parse(f)
    print(f"Train 1: {calc_1(d)}")
    print(f"Train 2: {calc_2(d)}")

with open("./2025/02/data.txt") as f:
    d = parse(f)
    print(f"Actual 1: {calc_1(d)}")
    print(f"Actual 2: {calc_2(d)}")
