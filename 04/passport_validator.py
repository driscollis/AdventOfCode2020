data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

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
    if len(dd['byr']) != 4:
        return False
    if len(dd['iyr']) != 4:
        return False
    if len(dd['eyr']) != 4:
        return False

    if '1920' > dd['byr'] or dd['byr'] > '2002':
        return False
    if dd['iyr'] < "2010" or dd['iyr'] > "2020":
        return False
    if dd['eyr'] < "2020" or dd['eyr'] > "2030":
        return False
    if not any([dd['hgt'].find('in'), dd['hgt'].find('cm')]):
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
    return True


def count_passports(data: str) -> int:
    pport = {}
    s = ''
    count = 0
    for line in data.split('\n'):
        if line.strip() == '':
            # process
            count += bool(process2(s))
            s = ''
        s += ' ' + line
    print(f"Valid passports: {count}")
    return count

if __name__ == '__main__':
    with open('input.txt') as f:
        data = f.read()
    count_passports(data)