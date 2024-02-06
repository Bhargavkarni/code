def convert_str_to_integer(int_integer):
    new_list = []
    for item in range(len(int_integer)):
        int_integer[item] = int(int_integer[item])
        new_list.append(int_integer[item])
    return new_list
def unique_values(int_integer,k_num):
    stop_index = len(int_integer)-1
    unique_pair_set = set()
    for cur_index in range(stop_index):
        num_1 = int_integer[cur_index]
        num_2 = k_num - num_1
        remaining_list = int_integer[cur_index+1:]
        if num_2 in remaining_list:
            pair = (num_1,num_2)
            sorted_pair = tuple(sorted(pair))
            unique_pair_set.add(sorted_pair)
    return unique_pair_set
        

int_integer = input().split(",")
k_num = int(input())
first_int_integer = convert_str_to_integer(int_integer)
unique_pairs = unique_values(int_integer,k_num)
unique_pairs = list(unique_pairs)
unique_pairs.sort()
for pair in unique_pairs:
    print(pair)