with open('./data/10_1_input.txt') as txt_file:
    data_list = [int(x.strip()) for x in txt_file.readlines()]

# data_list = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

data_list.append(0)
data_list.append(max(data_list) + 3)

data_dict = {}

for x in data_list:
    for y in range(3):
        lookup_value = x + y + 1

        if lookup_value in data_list:
            if x not in data_dict:
                data_dict[x] = list()

            data_dict[x].append(lookup_value)


memo = {}


def path_tracer(position):

    if position == max(data_list):
        return 1

    if position in memo:
        return memo[position]

    collector = 0

    for next_position in data_dict[position]:

        collector += path_tracer(next_position)

    memo[position] = collector

    return collector


print(data_dict)
print(path_tracer(0))
print(len(memo))
