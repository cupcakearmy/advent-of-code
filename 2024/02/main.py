def is_safe_1(numbers, tolerance=0) -> bool:
    if len(numbers) < 2:
        return True

    down = numbers[0] > numbers[1]
    cur = numbers[0]
    for i in range(1, len(numbers)):
        x = numbers[i]
        diff = x - cur
        if down:
            diff *= -1
        if 3 < diff or diff < 1:
            if tolerance == 0:
                return False
            else:
                found = set()
                for j in range(len(numbers)):
                    tmp = numbers[:]
                    del tmp[j]
                    if is_safe_1(tmp, tolerance - 1):
                        found.add(tuple(tmp))
                        # print("adding", tuple(tmp))
                        return True
                        break
                else:
                    # return False
                    pass

                # print(len(found))

                first_removed = numbers[:]
                del first_removed[i - 1]
                if is_safe_1(first_removed, tolerance - 1):
                    return True
                second_removed = numbers[:]
                del second_removed[i]
                if is_safe_1(second_removed, tolerance - 1):
                    return True

                if len(found) > 0:
                    print(numbers, i, x)
                    print(first_removed, second_removed)
                    print(numbers, found)
                return False
        cur = x
    return True


def is_safe_2(numbers, tolerance=0):
    # Convert to differences
    diffs = [0]  # First element is zero, as there is no predecessor
    for i in range(1, len(numbers)):
        diffs.append(numbers[i] - numbers[i - 1])
    print(numbers, diffs)


def solve(raw: str) -> int:
    # Part 1
    part1 = 0
    part2 = 0

    for line in raw.splitlines():
        numbers = [int(x) for x in line.split(" ")]
        if is_safe_2(numbers):
            part1 += 1
        if is_safe_2(numbers, 1):
            part2 += 1

    return (part1, part2)


# Test
with open("./2024/02/test.txt", "r") as f:
    result = solve(f.read().strip())
    print(result)

# Input
# with open("./2024/02/input.txt", "r") as f:
#     result = solve(f.read().strip())
#     print(result)
