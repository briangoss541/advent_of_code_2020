with open('./data/12_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

# data_list = ['F10', 'N3', 'F7', 'R90', 'F11']

print(data_list)


def instruction_handler(input_data):

    for action in input_data:

        act_type = action[0]
        act_value = int(action[1:])

        waypoint_x = waypoint_vector['x']
        waypoint_y = waypoint_vector['y']

        if act_type == 'N':
            waypoint_vector['y'] += act_value
        elif act_type == 'S':
            waypoint_vector['y'] -= act_value
        elif act_type == 'E':
            waypoint_vector['x'] += act_value
        elif act_type == 'W':
            waypoint_vector['x'] -= act_value
        elif act_type in ('L', 'R') and act_value == 180:
            waypoint_vector['x'] = -waypoint_x
            waypoint_vector['y'] = -waypoint_y
        elif (act_type == 'R' and act_value == 90) or (act_type == 'L' and act_value == 270):
            waypoint_vector['x'] = waypoint_y
            waypoint_vector['y'] = -waypoint_x
        elif (act_type == 'L' and act_value == 90) or (act_type == 'R' and act_value == 270):
            waypoint_vector['x'] = -waypoint_y
            waypoint_vector['y'] = waypoint_x
        elif act_type == 'F':
            move_coord = {
                'x': waypoint_vector['x'] * act_value,
                'y': waypoint_vector['y'] * act_value
            }

            ship_coord['x'] += move_coord['x']
            ship_coord['y'] += move_coord['y']

        print(ship_coord)
        print(waypoint_vector)
        print('\n')


ship_coord = {'x': 0,
              'y': 0}

waypoint_vector = {'x': 10,
                   'y': 1}

instruction_handler(data_list)

print(abs(ship_coord['x']) + abs(ship_coord['y']))
