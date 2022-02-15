import comparison
import pandas
# a function that takes a row-size list (of format [row1,size1,row2,size2]) and the split the list into two lists [row1,row2],[size1,size2]


column_name_response = input(
    'Name of the column where you want to output the data (all caps): ')


def row_size_list_splitter(list1):

    row_list = []
    size_list = []

    for item in range(list1.__len__()):

        if item % 2 == 0:
            rows = int(list1.__getitem__(item))
            row_list.append(rows)

        if item % 2 != 0:
            size = list1.__getitem__(item)
            size_list.append(size)

    return row_list, size_list


row_list, size_list = row_size_list_splitter(comparison.row_size_list)


# a function that takes the adds size from size_list in rows according to row_list and in the column given by column_name of the already given format (excel) in only_column_xlsx
def table_output(row_list, size_list, only_column_xlsx, column_name):

    df = pandas.read_excel(only_column_xlsx)

    x = 0
    for rows in row_list:

        size_data = size_list.__getitem__(x)
        df.at[rows-2, column_name] = size_data
        x += 1

    output_file = open('OUTPUT.txt', 'w')
    output_file.write(str(df))
    output_file.close

    return df


output_dataframe = table_output(
    row_list, size_list, 'only_column.xlsx', column_name_response)

print(f'The only_column.xlsx has been modified and stored in ouput.txt')
