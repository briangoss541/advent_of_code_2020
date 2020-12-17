with open('./data/16_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

# print(data_list)

def data_processor(input_data):

    first_space = input_data.index('')
    second_space = input_data[first_space + 1:].index('') + first_space + 1

    rules_dict = dict()
    all_rule_value_set = set()

    nearby_tickets = list()

    your_ticket = None

    for row in input_data[:first_space]:

        rule_name, rule_data = row.split(': ')

        rule_data_ranges = rule_data.split(' or ')

        point_rule_set = set()

        for rule_range in rule_data_ranges:

            start_value, end_value = rule_range.split('-')

            point_rule_set.update({x for x in range(int(start_value), int(end_value) + 1)})
            all_rule_value_set.update({x for x in range(int(start_value), int(end_value) + 1)})

        rules_dict.update({rule_name: point_rule_set})

    for row in input_data[first_space + 1:second_space]:

        if row == 'your ticket:':
            continue

        your_ticket = [int(x) for x in row.split(',')]

    for row in input_data[second_space + 1:]:

        if row == 'nearby tickets:':
            continue

        nearby_tickets.append([int(x) for x in row.split(',')])

    return all_rule_value_set, your_ticket, nearby_tickets, rules_dict


def field_index_check(input_index):
    for ticket in nearby_tickets:

        target_value = ticket[input_index]

        if int(target_value) not in overall_rule_set:
            continue

        if int(target_value) not in field_set:
            return False

    return True


overall_rule_set, my_ticket, nearby_tickets, field_dict = data_processor(data_list)

field_count = len(nearby_tickets[0])

# print(field_dict)

outcome_dict = dict()

for field_name in field_dict.keys():

    field_set = field_dict[field_name]

    for field_index in range(field_count):

        field_result = field_index_check(field_index)

        if field_result is True:

            if field_name not in outcome_dict:
                outcome_dict[field_name] = list()

            outcome_dict[field_name].append(field_index)

spot_claiming = dict()

for field_name in sorted(outcome_dict, key=lambda x: len(outcome_dict[x]), reverse=False):

    remaining_field = list(set(outcome_dict[field_name]) - set(spot_claiming.values()))

    spot_claiming.update({
        field_name: remaining_field[0]
    })

my_ticket_product = 1

for field_name, field_index in spot_claiming.items():

    if 'departure' in field_name:

        my_ticket_product *= my_ticket[field_index]

print(my_ticket_product)
