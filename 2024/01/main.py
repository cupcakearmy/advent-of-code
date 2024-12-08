from typing import List


def calc(raw: str) -> int:
    left: List[int] = []
    right: List[int] = []
    for line in raw.splitlines():
        [left_raw, right_raw] = line.split("   ")
        left.append(int(left_raw))
        right.append(int(right_raw))

    left.sort()
    right.sort()

    # Part 1
    part1 = 0
    for i in range(len(left)):
        diff = abs(left[i] - right[i])
        part1 += diff

    # Part 2
    part2 = 0
    counts = {}
    for x in right:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    for x in left:
        if x in counts:
            part2 += x * counts[x]

    return (part1, part2)


# Test
with open("./2024/01/test.txt", "r") as f:
    result = calc(f.read().strip())
    print(result)

# Input
with open("./2024/01/input.txt", "r") as f:
    result = calc(f.read().strip())
    print(result)
