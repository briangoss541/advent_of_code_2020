with open('./data/16_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

print(data_list)

def data_processor(input_data):

    first_space = input_data.index('')
    second_space = input_data[first_space + 1:].index('') + first_space + 1

    rules_dict = dict()
    rule_value_set = set()

    nearby_tickets = list()

    your_ticket = None

    for row in input_data[:first_space]:

        rule_name, rule_data = row.split(': ')

        rule_data_ranges = rule_data.split(' or ')

        for rule_range in rule_data_ranges:

            start_value, end_value = rule_range.split('-')

            rule_value_set.update({x for x in range(int(start_value), int(end_value) + 1)})

    for row in input_data[first_space + 1:second_space]:

        if row == 'your ticket:':
            continue

        your_ticket = [int(x) for x in row.split(',')]

    for row in input_data[second_space + 1:]:

        if row == 'nearby tickets:':
            continue

        nearby_tickets.append([int(x) for x in row.split(',')])


    return rule_value_set, your_ticket, nearby_tickets


rule_set, my_ticket, nearby_tickets = data_processor(data_list)

invalid_list = list()

for ticket in nearby_tickets:

    for target_value in ticket:

        if int(target_value) not in rule_set:
            invalid_list.append(int(target_value))

print(sum(invalid_list))
