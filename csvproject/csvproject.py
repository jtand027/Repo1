import csv
from collections import defaultdict

def find_csv_duplicates(csv_file):
    """
    Reads a CSV file, stores its values in a dictionary, and finds duplicates.

    :param csv_file: Path to the input CSV file.
    """
    value_counts = defaultdict(int)  # Dictionary to store counts of each value
    duplicates = {}  # Dictionary to store duplicate values and their counts

    try:
        with open(csv_file, mode='r', encoding='utf-8') as csv_file_obj:
            csv_reader = csv.reader(csv_file_obj)

            # Process each row in the CSV file
            for row in csv_reader:
                for value in row:
                    value_counts[value] += 1

            print(value_counts)

        quit()
        # Identify duplicates
        duplicates = {value: count for value, count in value_counts.items() if count > 1}

        # Print results
        if duplicates:
            print("Duplicate values found:")
            for value, count in duplicates.items():
                print(f"Value: {value} - Occurrences: {count}")
        else:
            print("No duplicate values found.")

    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
csv_file_path = './file.csv'  

find_csv_duplicates(csv_file_path)
