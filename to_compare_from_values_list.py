import os

directory_of_pcapng = input("Directory where the pcapng files are stored: ")

# a function that makes a list of size in kb and file names


def size_filename_list(input_dir):

    sub_dir = os.listdir(input_dir)

    stats_list = [[os.stat(os.path.join(
        directory_of_pcapng, filename)).st_size//1024, filename] for filename in sub_dir]

    return stats_list


stats_list = size_filename_list(directory_of_pcapng)

# a function that makes the list of format [size,hourmin]


def stat_list_splitter(input_list):

    modified_stat_list = []

    for stat in input_list:
        size = stat.__getitem__(0)

        clean_file_name = stat.__getitem__(1)
        clean_file_name = clean_file_name[11:15]

        modified_stat_list.append(size)
        modified_stat_list.append(clean_file_name)

    return modified_stat_list


modified_stat_list = stat_list_splitter(stats_list)

# print(modified_stat_list)
