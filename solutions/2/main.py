from os.path import join, dirname


def checkRow(row: str, alternative=False) -> bool:
    rule, password = map(lambda s: s.strip(), row.split(':'))
    amount, char = rule.split(' ')
    minimum, maximum = map(int, amount.split('-'))
    if alternative:
        return (password[minimum - 1] == char) ^ (password[maximum - 1] == char)
    else:
        occurrences = password.count(char)
        return minimum <= occurrences <= maximum


data = join(dirname(__file__), 'data.txt')
with open(data) as f:
    valid = 0
    valid_alt = 0
    rows = list(f.read().strip().split('\n'))
    for row in rows:
        if(checkRow(row)):
            valid += 1
        if(checkRow(row, alternative=True)):
            valid_alt += 1
    print(f'Found {valid} valid passwords.')
    print('Policy changed...')
    print(f'Found {valid_alt} valid passwords.')
