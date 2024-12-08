import re

re_mul = re.compile(r"mul\(\d+,\d+\)")
re_enable = re.compile(r"do\(\)")
re_disable = re.compile(r"don't\(\)")


def solve(raw: str) -> int:
    # Part 1
    part1 = 0
    part2 = 0

    enable = [m.end() for m in re_enable.finditer(raw)]
    disable = [m.end() for m in re_disable.finditer(raw)]
    for match in re_mul.finditer(raw):
        # Part 1
        [left, right] = match.group()[4:-1].split(",")
        result = int(left) * int(right)
        part1 += result

        # Part 2
        s = match.start()
        last_enable = 0
        for x in enable:
            if x > s:
                break
            last_enable = x
        last_disable = 0
        for x in disable:
            if x > s:
                break
            last_disable = x

        disabled = last_disable != 0 and last_disable > last_enable
        if disabled:
            continue
        part2 += result
    return (part1, part2)


# Test
with open("./2024/03/test.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)

# Input
with open("./2024/03/input.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)
