
def main():
    password_file = '2_passwords.txt'

    with open(password_file, 'r') as f:
        passwords = [line.rstrip('\n') for line in f]

    data = get_min_max_letter(passwords)
    valid_count = count_valid_passwords_part_1(data)
    print(f'Part 1: {valid_count}')

    valid_count = count_valid_passwords_part_2(data)
    print(f'Part 2: {valid_count}')


def get_min_max_letter(passwords):
    ret_val = []
    for item in passwords:
        items = item.split()
        min_val, max_val = [int(x) for x in items[0].split('-')]
        letter = items[1][:-1]
        password = items[2]
        ret_val.append({'min_val': min_val, 'max_val': max_val, 'letter': letter, 'password': password})
    return ret_val


def count_valid_passwords_part_1(data):
    ret_val = 0
    for item in data:
        # if item[0] <= item[3].count(item[2]) <= item[1]:
        if item['min_val'] <= item['password'].count(item['letter']) <= item['max_val']:
            ret_val += 1

    return ret_val


def count_valid_passwords_part_2(data):
    ret_val = 0

    def is_in_min():
        if item['password'][item['min_val'] - 1] == item['letter']:
            return True

    def is_in_max():
        if item['password'][item['max_val'] - 1] == item['letter']:
            return True
    for item in data:
        a = is_in_min()
        b = is_in_max()
        if (a and not b) or (b and not a):
            ret_val += 1

    return ret_val


if __name__ == '__main__':
    main()
