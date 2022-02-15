input('to_compare_to_values.txt should be present')
input('no two pcapng files should have the same name \nPress any key to continue.....')


txt_file = 'to_compare_to_values.txt'

# making a list of values from to_compare_to_values.txt


def to_compare_list(input_txt_file):

    with open(input_txt_file, 'r') as file:
        data_list = [entry.strip() for entry in file.readlines()]
    return data_list


data_list = to_compare_list(txt_file)

# a function that splits the row number and the time from data_list


def to_compare_list_splitter(input_list):

    split_data_list = []

    for item in data_list:
        each_item_row_number = item[0:2]
        each_item_time = item[2:]

        split_data_list.append(each_item_row_number)
        split_data_list.append(each_item_time)

    return split_data_list


split_data_list = to_compare_list_splitter(data_list)

# print(split_data_list)
