with open('./data/8_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]


def parse_bootcode(input_data):

    instruction_dict = dict()

    for index, code in enumerate(input_data):

        op_code, argument = code.split(' ')

        instruction_dict.update({index: {'operation': op_code,
                                         'argument': argument}})

    return instruction_dict


def code_tracer(input_instructions, pointer):

    point_operation = input_instructions[pointer]['operation']
    point_arg = input_instructions[pointer]['argument']

    if point_operation == 'acc':
        acc_value = int(point_arg)
    else:
        acc_value = 0

    if point_operation == 'jmp':
        new_point = pointer + int(point_arg)
    else:
        new_point = pointer + 1

    return acc_value, new_point


def code_handler(input_instructions):

    accumulator = 0
    current_pointer = 0
    visited_points = list()

    while current_pointer <= len(input_instructions) - 1:

        acc_to_add, next_pointer = code_tracer(input_instructions, current_pointer)

        visited_points.append(current_pointer)

        if len(visited_points) == len(set(visited_points)):
            accumulator += acc_to_add
        else:
            # print("Pointer reused. Exiting.")
            return None

        current_pointer = next_pointer

    return accumulator


def code_editor(input_instructions):

    for line, line_data in input_instructions.items():

        if line_data['operation'] == 'jmp':

            input_instructions[line]['operation'] = 'nop'

            test_result = code_handler(input_instructions)

            input_instructions[line]['operation'] = 'jmp'

            if test_result is not None:
                print(test_result)

        elif line_data['operation'] == 'nop':

            input_instructions[line]['operation'] = 'jmp'

            test_result = code_handler(input_instructions)

            input_instructions[line]['operation'] = 'nop'

            if test_result is not None:
                print(test_result)


instructions = parse_bootcode(data_list)

code_editor(instructions)
