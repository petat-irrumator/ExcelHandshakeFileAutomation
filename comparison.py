import to_compare_from_values_list
import to_compare_to_values_list


# this function takes two list compares their even items then get the item before them from each of the list

def compare_list(list1, list2):
    # list 1 is the values to compare from
    # list 2 is the values to compare to
    row_size_list = []
    for list1_item in range(list1.__len__()):
        if list1_item % 2 != 0:

            list1_item_to_compare = list1.__getitem__(list1_item)

            for list2_item in range(list2.__len__()):
                if list2_item % 2 != 0:
                    list2_item_to_compare = list2.__getitem__(list2_item)

                    if list1_item_to_compare == list2_item_to_compare:

                        size_of_filename = list1.__getitem__(list1_item-1)
                        row_number = list2.__getitem__(list2_item-1)

                        row_size_list.append(row_number)
                        row_size_list.append(size_of_filename)
    return row_size_list


row_size_list = compare_list(list1=to_compare_from_values_list.modified_stat_list,
                             list2=to_compare_to_values_list.split_data_list)

# print(row_size_list)
