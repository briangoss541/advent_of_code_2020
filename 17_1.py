with open('./data/17_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

# print(data_list)

def list_to_coords(input_data):

    start_range = -6
    end_range = len(input_data[0]) + 6

    result_dict = {(x, y, z): 0 for x in range(start_range, end_range) for y in range(start_range, end_range) for z in range(start_range, end_range)}

    for y_index, row in enumerate(input_data):
        for x_index, column in enumerate(row):
            if column == '#':
                result_dict.update({
                    (x_index, y_index, 0): 1
                })
            elif column == '.':
                result_dict.update({
                    (x_index, y_index, 0): 0
                })

    return result_dict


def adjacent_counter(x_position, y_position, z_position, round_dict):

    coords_to_check = [(x, y, z) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1]]
    coords_to_check.remove((0, 0, 0))

    filled_count = 0

    for x_move, y_move, z_move in coords_to_check:

        x_check = x_position + x_move
        y_check = y_position + y_move
        z_check = z_position + z_move

        if (x_check, y_check, z_check) in round_dict:
            if round_dict[(x_check, y_check, z_check)] == 1:
                filled_count += 1
        else:
            print(f'Made it out of bounds with {x_check, y_check, z_check}')

    return filled_count


def rule_abider():

    round_num = 1

    while round_num <= 6:

        round_coord_dict = coord_dict.copy()

        for coord_target, coord_status in coord_dict.items():

            seat_count = adjacent_counter(coord_target[0], coord_target[1], coord_target[2], round_coord_dict)

            if coord_status == 1 and seat_count not in (2, 3):
                coord_dict[coord_target] = 0
            if coord_status == 0 and seat_count == 3:
                coord_dict[coord_target] = 1

        round_num += 1


coord_dict = list_to_coords(data_list)

rule_abider()

result_count = sum([x for x in coord_dict.values()])
print(result_count)
