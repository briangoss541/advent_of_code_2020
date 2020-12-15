from itertools import count

with open('./data/13_1_input.txt') as txt_file:
    data_list = [x.strip() for x in txt_file.readlines()]

# data_list = ['939', '7,13,x,x,59,x,31,19']

bus_list = [x for x in data_list[1].split(',')]

timestamp = 0

bus_times = [(index, int(bus)) for index, bus in enumerate(bus_list) if bus != 'x']


def time_traveler(input_times):

    # noblematt20 on Reddit gave the push through to the best way to step
    # https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfncyoc?utm_source=share&utm_medium=web2x&context=3

    step = 1
    starting_point = 0

    for offset, bus_period in input_times:

        starting_point = next(c for c in count(starting_point, step) if (c + offset) % bus_period == 0)
        step *= bus_period

    return starting_point

    # Old, SLOW code
    # for start_time in count(start=0, step=input_times[0][1]):
    #
    #     iter_flag = True
    #
    #     for offset, bus in input_times:
    #
    #         target_time = start_time + offset
    #
    #         if target_time % bus != 0:
    #             iter_flag = False
    #             break
    #
    #     if iter_flag is True:
    #         return start_time


# end_time = time_traveler(sized_new_times)

print(bus_times)

end_time = time_traveler(bus_times)
print(end_time)

