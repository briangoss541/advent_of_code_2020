with open('./data/2_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]


def policy_parser(input_policy):

    occurrence_policy, target_letter = input_policy.split(' ')

    low_occurrence, high_occurrence = occurrence_policy.split('-')

    return {'target': target_letter,
            'low': int(low_occurrence),
            'high': int(high_occurrence)}


def password_validator(input_pass, input_policy):

    letter_list = [x for x in input_pass]

    letter_count = [x for x in letter_list if x == input_policy['target']]

    if input_policy['low'] <= len(letter_count) <= input_policy['high']:
        return True
    else:
        return False


valid_collector = 0

for row in data_list:

    row_policy, row_password = row.split(': ')

    policy_dict = policy_parser(row_policy)

    valid_resp = password_validator(row_password, policy_dict)

    if valid_resp is True:
        valid_collector += 1

print(f"Found {valid_collector} valid passwords.")
