with open('./data/5_1_input.txt') as txt_file:

    data_list = [x.strip() for x in txt_file.readlines()]


def row_col_selector(input_string):

    return input_string[:7], input_string[7:]


def row_parser(input_inst):

    binary_value = input_inst.replace('F', '0').replace('B', '1')

    return int(binary_value, 2)


def col_parser(input_inst):

    binary_value = input_inst.replace('L', '0').replace('R', '1')

    return int(binary_value, 2)


def seat_id(input_row, input_col):

    return input_row * 8 + input_col


seat_id_list = list()
for row in data_list:
    row_string, col_string = row_col_selector(row)

    row_dec = row_parser(row_string)
    col_dec = col_parser(col_string)

    seat_id_list.append(seat_id(row_dec, col_dec))

print(f"The top seat ID is {max(seat_id_list)}")
