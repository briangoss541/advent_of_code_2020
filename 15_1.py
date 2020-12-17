data_list = [12, 1, 16, 3, 11, 0]
# data_list = [0, 3, 6]

memory_dict = dict()


def speak_memory():

    turn_count = 1
    spoken_number = None

    while turn_count <= 2020:

        # Starting numbers
        if turn_count <= len(data_list):

            spoken_number = data_list[turn_count - 1]

            memory_dict[spoken_number] = [turn_count, ]

        else:
            if spoken_number in memory_dict and len(memory_dict[spoken_number]) >= 2:  # Aged numbers

                age = memory_dict[spoken_number][-1] - memory_dict[spoken_number][-2]

                if age in memory_dict:
                    memory_dict[age].append(turn_count)
                else:
                    memory_dict[age] = [turn_count, ]

                spoken_number = age

            else:  # First-timers

                if 0 in memory_dict:
                    memory_dict[0].append(turn_count)
                else:
                    memory_dict[0] = [turn_count, ]

                spoken_number = 0

        turn_count += 1

    return spoken_number


final_num = speak_memory()
print(final_num)
