from math import ceil

with open('./data/3_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]


def string_repeater_and_finder(input_string, pos_to_find):

    target_length = ceil((pos_to_find + 1) / len(input_string))

    repeated_string = input_string * target_length

    tree_list = [x for x in repeated_string]

    return tree_list[pos_to_find]


def tree_locator(input_char):

    if input_char in ('#',):
        return True
    else:
        return False


test_string = '..#......###....#...##..#.#....'

list_of_slopes = [
    {'x': 1, 'y': 1},
    {'x': 1, 'y': 3},
    {'x': 1, 'y': 5},
    {'x': 1, 'y': 7},
    {'x': 2, 'y': 1},
]

trees_meta_collection_list = list()

for slope in list_of_slopes:

    tree_collector = 0

    x_pos = 0
    y_pos = 0

    for index, tree_row in enumerate(data_list):

        if index == x_pos:

            location = string_repeater_and_finder(tree_row, y_pos)

            tree_resp = tree_locator(location)

            if tree_resp is True:
                tree_collector += 1

            x_pos += slope['x']
            y_pos += slope['y']

    trees_meta_collection_list.append(tree_collector)

    print(f"Slope {slope} hits {tree_collector} trees.")

print(trees_meta_collection_list)

total_count = 1
for count in trees_meta_collection_list:
    total_count = count * total_count

print(f'With a total count of {total_count}')
