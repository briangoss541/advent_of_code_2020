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


def sum_check(data_window, target_num):
    check_list = [(x, y) for x in data_window for y in data_window]

    for check_x, check_y in check_list:

        if check_x == check_y:
            continue

        if check_x + check_y == target_num:
            return True

    return False


def window_handler(input_data):
    pointer = 0
    window_size = 25

    for _ in range(len(input_data)):

        valid_flag = sum_check(input_data[pointer:pointer + window_size], input_data[pointer + window_size + 1])

        if valid_flag is False:
            print(f"Pointer: {pointer}")
            print(f"Failing input number: {input_data[pointer + window_size + 1]}")

        pointer += 1

    print(f"Pointer: {pointer}")
    print(f"Failing input number: {input_data[pointer + window_size + 1]}")


test_list = [40090, 40043, 55249, 57897, 42058, 45149, 52712, 48234, 48302, 72946, 50089, 64342, 52879, 103551, 57104, 72428, 62191, 79837, 63920, 71215, 73138, 80133, 84587, 82148, 156430]

for x in test_list:

    if (152323 - x) in test_list:
        print(x, 152323 - x)

window_handler(data_list)
