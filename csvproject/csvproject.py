import csv
from collections import defaultdict
from pprint import pprint

def find_csv_duplicates(csv_file):
    """
    Reads a CSV file, stores its values in a dictionary, and finds duplicates.

    :param csv_file: Path to the input CSV file.
    """
    # col_value_counts is a dictionary that stores the count / first line number of each value by column
    #    key:   column index
    #    value: dict (key: column value, value: tuple (count of the value, line number of the first occurrence))
    col_value_counts = defaultdict(dict)

    try:
        with open(csv_file, mode='r', encoding='utf-8') as csv_file_obj:
            csv_reader = csv.reader(csv_file_obj)

            # Process each row in the CSV file
            cur_line_num = 1
            for row in csv_reader:
                # iterate over each column in the row and update the col_value_counts dictionary accordingly
                for row_col_idx, row_col_value in enumerate(row):
                    # get the column index dictionary
                    tmp_col_val_dict = col_value_counts.get(row_col_idx, None)

                    # is the first time we're seeing this column?
                    if tmp_col_val_dict is None:
                        # store a tuple containing the a count value of 1 and the line number of the first occurrence
                        col_value_counts[row_col_idx] = {row_col_value: (1, cur_line_num)}
                    else:
                        # get the dictionary for the current column value
                        tmp_dict = tmp_col_val_dict.get(row_col_value, None)

                        # is this the first time seeing this value in this column?
                        if tmp_dict is None:
                            # update the column index dictionary
                            col_value_counts[row_col_idx][row_col_value] = (1, cur_line_num)
                        else:
                            # increment the count of the value (but keep the line number of the first occurrence - which never changes)
                            col_value_counts[row_col_idx][row_col_value] = (tmp_dict[0] + 1, tmp_dict[1])

                # increment the line number so we can inspect the next line
                cur_line_num += 1


        # print the working dictionary
        print("Working dictionary:")
        pprint(col_value_counts)
        print("\n-----------------------------------\n")
        
        # Identify duplicates in the first column (column 0)
        # Iterate through the col_value_counts dictrionary for column 0
        print("List out the duplicates in the first column:")
        for value, (count, line_num) in col_value_counts[0].items():
            if count > 1:
                print(f"{value} - line: {line_num} - number of duplicates: {count}")

    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file_path = './file.csv'  

find_csv_duplicates(csv_file_path)
