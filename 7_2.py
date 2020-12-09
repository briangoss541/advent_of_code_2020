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
#
# data_list = [
#     'shiny gold bags contain 2 dark red bags.',
#     'dark red bags contain 2 dark orange bags.',
#     'dark orange bags contain 2 dark yellow bags.',
#     'dark yellow bags contain 2 dark green bags.',
#     'dark green bags contain 2 dark blue bags.',
#     'dark blue bags contain 2 dark violet bags.',
#     'dark violet bags contain no other bags.'
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


def bag_nest_handler(bag_data, start_bag):

    nest_collection = 0

    for child_bag in bag_data[start_bag]:

        child_bag_count = bag_data[start_bag][child_bag]

        nest_collection += (child_bag_count * bag_nester(bag_data, child_bag))

    return nest_collection


def bag_nester(bag_data, parent_bag):

    level_collector = 1

    if bag_data[parent_bag] is None:
        return level_collector

    for child_bag in bag_data[parent_bag]:

        child_bag_count = bag_data[parent_bag][child_bag]

        child_collection = bag_nester(bag_data, child_bag)

        level_collector += (child_bag_count * child_collection)

    return level_collector


bag_dict = rule_parser(data_list)

total_count = bag_nest_handler(bag_dict, 'shiny gold')

print(f"The count for the bag is {total_count}")
