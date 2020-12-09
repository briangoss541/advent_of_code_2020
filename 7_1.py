with open('./data/7_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]


# data_list = [
#     'light red bags contain 1 bright white bag, 2 muted yellow bags.',
#     'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#     'bright white bags contain 1 shiny gold bag.',
#     'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#     'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#     'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#     'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#     'faded blue bags contain no other bags.',
#     'dotted black bags contain no other bags.'
# ]


def rule_parser(input_data):

    bag_rules = dict()

    for row in input_data:

        bag_name, bag_data = row.split(' bags contain ')

        if bag_data == 'no other bags.':
            bag_rules.update({bag_name: None})
            continue
        else:
            bag_rules[bag_name] = dict()

        for bag_sub_rule in bag_data.split(', '):

            sub_rule_split = bag_sub_rule.split(' ')

            bag_rules[bag_name].update({sub_rule_split[1] + ' ' + sub_rule_split[2]: int(sub_rule_split[0])})

    return bag_rules


def bag_trace_handler(bag_data, target_bag):

    good_bags = list()

    for bag_name_to_check in bag_data:

        tracer_resp = bag_tracer(bag_data, bag_name_to_check, target_bag)

        if tracer_resp is True:
            good_bags.append(bag_name_to_check)

    return good_bags


def bag_tracer(bag_data, bag_pointer, target_bag):

    if bag_data[bag_pointer] is None:
        return False

    if target_bag in bag_data[bag_pointer]:
        return True

    for sub_bag in bag_data[bag_pointer]:

        sub_check = bag_tracer(bag_data, sub_bag, target_bag)

        if sub_check is True:
            return True


bag_dict = rule_parser(data_list)

good_resp = bag_trace_handler(bag_dict, 'shiny gold')

print(len(good_resp))
