with open('./data/14_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

# data_list = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
#              'mem[8] = 11',
#              'mem[7] = 101',
#              'mem[8] = 0']


def mask_that_bit(input_mask, decimal_target):

    binary_target = '{0:036b}'.format(int(decimal_target))

    masked_binary_list = list()

    for index, bit in enumerate(input_mask):

        if bit == 'X':
            masked_binary_list.append(binary_target[index])
        else:
            masked_binary_list.append(bit)

    return int(''.join(masked_binary_list), 2)


def instruction_handler(input_data):

    bitmask = None

    for row in input_data:

        if 'mask' in row:

            bitmask = row.split('= ')[1]

        elif 'mem' in row:

            mem_arg, dec_value = row.split(' = ')

            mem_address = int(''.join([x for x in mem_arg if x.isnumeric()]))

            masked_value = mask_that_bit(bitmask, dec_value)

            memory_dict.update({
                mem_address: masked_value
            })


memory_dict = dict()

instruction_handler(data_list)

print(memory_dict)

print(f'Sum is {sum(memory_dict.values())}')
