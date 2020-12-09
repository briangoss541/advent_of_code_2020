with open('./data/6_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

print(data_list)


def customs_data_parser(input_list):
    results_list = list()
    target_group = list()

    for line in input_list:

        if line == '':
            results_list.append(target_group)
            target_group = list()
            continue

        target_group.append(line)

    results_list.append(target_group)

    return results_list


def group_customs_overlaps(input_group_data):
    overlap_set = set(input_group_data[0])

    for person_data in input_group_data[1:]:

        person_set = set()

        for answer_char in list(person_data):
            person_set.add(answer_char)

        overlap_set = person_set & overlap_set

    return len(overlap_set)


def group_customs_with_sets(input_group_data):
    yes_set = set()

    for person_data in input_group_data:

        for answer_char in list(person_data):
            yes_set.add(answer_char)

    return len(yes_set)


customs_data = customs_data_parser(data_list)

count_collector = 0
for group_data in customs_data:
    yes_count = group_customs_overlaps(group_data)
    count_collector += yes_count

print(f"The sum of the counts is {count_collector}")
