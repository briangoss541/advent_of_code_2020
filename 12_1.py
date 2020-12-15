with open('./data/12_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

print(data_list)


def process_translations(input_data):

    for action in input_data:

        act_dir = action[0]
        act_mag = int(action[1:])

        if act_dir == 'N':
            origin_coord['y'] += act_mag
        elif act_dir == 'S':
            origin_coord['y'] -= act_mag
        elif act_dir == 'E':
            origin_coord['x'] += act_mag
        elif act_dir == 'W':
            origin_coord['x'] -= act_mag


def process_vectors(input_data):

    compass = 0

    for action in input_data:

        act_type = action[0]
        act_value = int(action[1:])

        if act_type == 'F':

            if compass == 0:
                origin_coord['x'] += act_value
            elif compass == 90:
                origin_coord['y'] += act_value
            elif compass == 180:
                origin_coord['x'] -= act_value
            elif compass == 270:
                origin_coord['y'] -= act_value
            else:
                print(f'Compass error {compass}')

        elif act_type == 'L':

            compass += act_value

        elif act_type == 'R':

            compass -= act_value

        if compass >= 360:
            compass -= 360
        elif compass < 0:
            compass += 360


origin_coord = {'x': 0,
                'y': 0}

process_translations(data_list)
process_vectors(data_list)

print(abs(origin_coord['x']) + abs(origin_coord['y']))
