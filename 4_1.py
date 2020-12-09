import json

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

    req_fields = {
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        # 'cid'
    }

    for req_field in req_fields:
        if req_field not in input_passport:
            return False

    if len(input_passport['byr']) != 4 or 1920 <= int(input_passport['byr']) <= 2002:
        return False




passport_data = passport_data_parser(data_list)

valid_count = 0
for passport in passport_data:
    valid_check = passport_validity_checker(passport)

    if valid_check is True:
        valid_count += 1

print(f"The number of valid passports is {valid_count}")
