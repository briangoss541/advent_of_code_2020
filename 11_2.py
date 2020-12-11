with open('./data/11_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

# data_list = ['L.LL.LL.LL', 'LLLLLLL.LL', 'L.L.L..L..', 'LLLL.LL.LL', 'L.LL.LL.LL', 'L.LLLLL.LL', '..L.L.....',
#              'LLLLLLLLLL', 'L.LLLLLL.L', 'L.LLLLL.LL']

# data_list = ['.......#.',
#              '...#.....',
#              '.#.......',
#              '.........',
#              '..#L....#',
#              '....#....',
#              '.........',
#              '#........',
#              '...#.....']


def list_to_coords(input_data):

    result_dict = {}

    for y_index, row in enumerate(input_data):
        for x_index, seat in enumerate(row):
            if seat == 'L':
                result_dict.update({
                    (x_index, y_index): 0
                })
            elif seat == '#':
                result_dict.update({
                    (x_index, y_index): 1
                })
            elif seat == '.':
                result_dict.update({
                    (x_index, y_index): -1
                })

    return result_dict


def adjacent_counter_star(x_position, y_position, round_dict):

    coords_to_check = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
    coords_to_check.remove((0, 0))

    filled_count = 0

    for x_move, y_move in coords_to_check:

        x_slope = x_move
        y_slope = y_move

        while True:
            x_check = x_position + x_move
            y_check = y_position + y_move

            if (x_check, y_check) in round_dict:
                if round_dict[(x_check, y_check)] == 1:
                    filled_count += 1
                    break
                elif round_dict[(x_check, y_check)] == 0:
                    break
            else:
                break

            x_move += x_slope
            y_move += y_slope

    return filled_count


def rule_abider():

    round_num = 1
    count_dict = {0: 0}

    while True:

        round_coord_dict = coord_dict.copy()

        for coord_target, coord_status in coord_dict.items():

            if coord_status == -1:
                continue

            seat_count = adjacent_counter_star(coord_target[0], coord_target[1], round_coord_dict)

            if coord_status == 0 and seat_count == 0:
                coord_dict[coord_target] = 1
            elif coord_status == 1 and seat_count >= 5:
                coord_dict[coord_target] = 0

        round_count = sum([x for x in coord_dict.values() if x != -1])
        # for coord_status in coord_dict.values():
        #     if coord_status is 1:
        #         round_count += 1

        count_dict[round_num] = round_count

        if count_dict[round_num] == count_dict[round_num - 1]:
            return round_count

        round_num += 1


coord_dict = list_to_coords(data_list)

print(coord_dict)

# print(adjacent_counter_star(3, 4, coord_dict))

output_count = rule_abider()

print(f"The stable output is {output_count}")
