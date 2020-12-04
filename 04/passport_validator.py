def process(lines: str) -> bool:
    """
    Part 1
    """
    d = lines.split(' ')
    dd = dict([item.split(':') for item in d if item])
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in keys:
        if key not in dd:
            return False
    return True


def process2(lines: str) -> bool:
    """
    Part 2
    """
    d = lines.split(' ')
    dd = dict([item.split(':') for item in d if item])

    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in keys:
        if key not in dd:
            return False

    if not any([dd[key] != 4 for key in ['byr', 'iyr', 'eyr']]):
        return False

    if '1920' > dd['byr'] or dd['byr'] > '2002':
        return False
    if dd['iyr'] < "2010" or dd['iyr'] > "2020":
        return False
    if dd['eyr'] < "2020" or dd['eyr'] > "2030":
        return False
    if not any(['in' in dd['hgt'], 'cm' in dd['hgt']]):
        return False
    if 'cm' in dd['hgt']:
        height = int(dd['hgt'][:-2])
        if height < 150 or height > 193:
            return False
    if 'in' in dd['hgt']:
        height = int(dd['hgt'][:-2])
        if height < 59 or height > 76:
            return False

    if '#' not in dd['hcl']:
        return False
    hcl = dd['hcl'].split('#')[-1]
    if len(hcl) != 6:
        return False

    try:
        int(hcl, 16)
    except ValueError:
        return False
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if dd['ecl'] not in eye_colors:
        return False
    if len(dd['pid']) != 9:
        return False

    if dd['pid'] == '182693366':
        print()
    return True


def count_passports(data: str) -> int:
    pport = {}
    s = ''
    count = 0
    passports = []
    for line in data.split('\n'):
        line = line.strip()
        if line == '':
            # process
            count += bool(process2(s))
            passports.append(s)
            s = ''
        s += ' ' + line
    print(f"Valid passports: {count}")
    return count

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    count_passports(data)