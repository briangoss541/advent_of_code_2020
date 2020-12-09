with open('./data/9_1_input.txt') as txt_file:
    data_list = [int(x.strip()) for x in txt_file.readlines()]

# print(data_list)

# data_list = [35,
#              20,
#              15,
#              25,
#              47,
#              40,
#              62,
#              55,
#              65,
#              95,
#              102,
#              117,
#              150,
#              182,
#              127,
#              219,
#              299,
#              277,
#              309,
#              576]


def num_set_check(data_list, target_num):

    for pointer in range(len(data_list)):

        for window_size in range(len(data_list) - pointer):

            accumulator = 0
            window_flag = True

            while window_flag is True:

                for x in range(window_size):

                    accumulator += data_list[pointer + x]

                    if accumulator == target_num:
                        return data_list[pointer:pointer + window_size]

                window_flag = False

    return None


results_list = num_set_check(data_list, 29221323)

print(max(results_list) + min(results_list))
