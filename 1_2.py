with open('./data/1_1_input.txt') as txt_file:
    data_list = [int(x.strip()) for x in txt_file.readlines()]

print(len(data_list))

for first_num in data_list:
    for second_num in data_list:
        for third_num in data_list:

            if first_num + second_num + third_num == 2020:
                print(f"Found {first_num} and {second_num} and {third_num}")
                print(f"Product is {first_num * second_num * third_num}")
