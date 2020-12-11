with open('./data/10_1_input.txt') as txt_file:
    data_list = [int(x.strip()) for x in txt_file.readlines()]

prev_volt = 0
volt_diff_dict = {1: 0,
                  3: 0}

for adapter_volt in sorted(data_list):

    if adapter_volt - prev_volt == 1:
        volt_diff_dict[1] += 1
    elif adapter_volt - prev_volt == 3:
        volt_diff_dict[3] += 1
    else:
        print('Error?')

    prev_volt = adapter_volt

print(f"{volt_diff_dict[1]} 1 differences, {volt_diff_dict[3] + 1} 3 differences")
print(f"Multiplied together is: {volt_diff_dict[1] * (volt_diff_dict[3] + 1)}")
