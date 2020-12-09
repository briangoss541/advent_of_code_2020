import re

with open('./data/4_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]


def passport_data_parser(input_data_list):
    results_list = list()
    target_passport = dict()

    for line in input_data_list:

        if line == '':
            results_list.append(target_passport)
            target_passport = dict()
            continue

        for kv_pair in line.split(' '):
            key, value = kv_pair.split(':')
            target_passport.update({key: value})

    results_list.append(target_passport)

    return results_list


def passport_validity_checker(input_passport):
    req_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid'
    ]

    for req_field in req_fields:
        if req_field not in input_passport:
            return False

    if len(input_passport['byr']) != 4 or not 1920 <= int(input_passport['byr']) <= 2002:
        return False

    if len(input_passport['iyr']) != 4 or not 2010 <= int(input_passport['iyr']) <= 2020:
        return False

    if len(input_passport['eyr']) != 4 or not 2020 <= int(input_passport['eyr']) <= 2030:
        return False

    if 'cm' in input_passport['hgt']:

        height_measure = input_passport['hgt'].split('cm')

        if len(height_measure) != 2 or not 150 <= int(height_measure[0]) <= 193:
            return False

    elif 'in' in input_passport['hgt']:

        height_measure = input_passport['hgt'].split('in')

        if len(height_measure) != 2 or not 59 <= int(height_measure[0]) <= 76:
            return False

    else:
        return False

    if input_passport['hcl'][0] == '#' and len(input_passport['hcl']) == 7:

        for hcl_char in input_passport['hcl'][1:]:

            if not re.match(r'[0-9]|[a-f]', hcl_char):
                return False
    else:
        return False

    if input_passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if not input_passport['pid'].isdecimal() or len(input_passport['pid']) != 9:
        return False

    return True


passport_data = passport_data_parser(data_list)

valid_count = 0
for passport in passport_data:
    valid_check = passport_validity_checker(passport)

    if valid_check is True:
        valid_count += 1

print(f"The number of valid passports is {valid_count}")
