import re


def main():
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open('4_passports.txt', 'r') as f:
        passports = [line.rstrip('\n') for line in f]

    # Gather all passports and break each down into a list of k:v pairs
    entry = ''
    entries = []
    for line in passports:
        if line == '':
            entries.append(entry.split())
            entry = ''
        else:
            entry += line + ' '
    # Put last passport into entries
    entries.append(entry.split())

    correct_passports = 0
    # For each entry count the number of valid fields
    for entry in entries:
        valid_field_count = 0
        for item in entry:
            k, v = item.split(':')
            if valid(k, v):
                valid_field_count += 1
        # Should be at least 7 valid fields
        if valid_field_count == len(valid_fields):
            correct_passports += 1
    print(correct_passports)


def valid(k: str, v: str) -> bool:
    """
    Checks the validity of a k:v pair.

    :param k: A key
    :param v: A value
    :return: if the key and value are valid
    """
    try:
        if 'byr' == k:
            return 1920 <= int(v) <= 2002
        elif 'iyr' == k:
            return 2010 <= int(v) <= 2020
        elif 'eyr' == k:
            return 2020 <= int(v) <= 2030
        elif 'hgt' == k:
            metric = v[-2:]
            value = int(v[:-2])
            if metric == 'in':
                return 59 <= value <= 76
            elif metric == 'cm':
                return 150 <= value <= 193
            return False
        elif 'hcl' == k:
            return False if re.search('^#([0-9]|[a-f]){6}$', v) is None else True
        elif 'ecl' == k:
            return v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        elif 'pid' == k:
            return False if re.search('^[0-9]{9}$', v) is None else True
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    main()
