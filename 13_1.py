with open('./data/13_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

# data_list = ['939', '7,13,x,x,59,x,31,19']

timestamp = int(data_list[0])
bus_list = [int(x) for x in data_list[1].split(',') if x != 'x']

modulo_dict = dict()

for bus in bus_list:
    modulo_dict.update({bus: (timestamp % bus) / bus})

modulo_sort = [(k, v) for k, v in sorted(modulo_dict.items(), key=lambda item: item[1], reverse=True)]

bus_id = modulo_sort[0][0]
bus_time = bus_id

while bus_time < timestamp:

    bus_time += bus_id

print((bus_time - timestamp) * bus_id)
