from os.path import join, dirname
import re


def validate_chunk(chunk, extended=False):
    parts = re.split(' |\n', chunk.strip())
    password = dict(map(lambda p: p.split(":"), parts))

    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if not all(item in password.keys() for item in required):
        return False

    if not extended:
        return True

    if not 1920 <= int(password['byr']) <= 2002:
        return False
    if not 2010 <= int(password['iyr']) <= 2020:
        return False
    if not 2020 <= int(password['eyr']) <= 2030:
        return False

    tmp = password['hgt']
    hgt = int(tmp[:-2])
    unit = tmp[-2:]
    if not unit in ['cm', 'in']:
        return False
    if unit == 'cm' and not 150 <= hgt <= 193:
        return False
    if unit == 'in' and not 59 <= hgt <= 76:
        return False

    if not re.match(r'^#[\dabcdef]{6}$', password['hcl']):
        return False
    if not re.match(r'^\d{9}$', password['pid']):
        return False

    if password['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    return True


data = join(dirname(__file__), '../data.txt')
with open(data) as f:
    chunks = re.split('\n\n+', f.read().strip())
    total_simple = 0
    total_extended = 0
    for chunk in chunks:
        total_simple += int(validate_chunk(chunk))
        total_extended += int(validate_chunk(chunk, extended=True))
    print(f'Simple Validation:\t{total_simple}')
    print(f'Extended Validation:\t{total_extended}')
