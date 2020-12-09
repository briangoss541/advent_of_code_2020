with open('./data/2_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]


def policy_parser(input_policy):

    occurrence_policy, target_letter = input_policy.split(' ')

    first_pos, second_pos = occurrence_policy.split('-')

    return {'target': target_letter,
            'first_pos': int(first_pos),
            'second_pos': int(second_pos)}


def password_validator(input_pass, input_policy):

    letter_list = [x for x in input_pass]

    try:
        first_check = letter_list[input_policy['first_pos'] - 1] == input_policy['target']
        second_check = letter_list[input_policy['second_pos'] - 1] == input_policy['target']
    except IndexError:
        return False

    if first_check is True and second_check is True:
        return False
    elif first_check is False and second_check is False:
        return False
    elif first_check is True or second_check is True:
        return True
    else:
        print('Error!')


valid_collector = 0

for row in data_list:

    row_policy, row_password = row.split(': ')

    policy_dict = policy_parser(row_policy)

    valid_resp = password_validator(row_password, policy_dict)

    if valid_resp is True:
        valid_collector += 1

print(f"Found {valid_collector} valid passwords.")
