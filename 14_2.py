from itertools import product

with open('./data/14_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]


def mask_that_bit(input_mask, decimal_target):

    binary_target = '{0:036b}'.format(int(decimal_target))

    output_values = list()

    masked_binary_list = list()

    floating_indexes = list()

    for index, bit in enumerate(input_mask):

        if bit == 'X':
            floating_indexes.append(index)
            masked_binary_list.append('X')
        elif bit == '0':
            masked_binary_list.append(binary_target[index])
        elif bit == '1':
            masked_binary_list.append('1')
        else:
            print('ERROR')

    float_product = product('01', repeat=len(floating_indexes))

    for product_values in float_product:
        for string_index, product_value in zip(floating_indexes, product_values):

            masked_binary_list[string_index] = product_value

        output_values.append(int(''.join(masked_binary_list), 2))

    return output_values


def instruction_handler(input_data):

    bitmask = None

    for row in input_data:

        if 'mask' in row:

            bitmask = row.split('= ')[1]

        elif 'mem' in row:

            mem_arg, dec_value = row.split(' = ')

            mem_address = int(''.join([x for x in mem_arg if x.isnumeric()]))

            masked_addresses = mask_that_bit(bitmask, mem_address)

            for masked_address in masked_addresses:

                memory_dict.update({
                    masked_address: int(dec_value)
                })


memory_dict = dict()

instruction_handler(data_list)

print(len(memory_dict))

print(f'Sum is {sum(memory_dict.values())}')
