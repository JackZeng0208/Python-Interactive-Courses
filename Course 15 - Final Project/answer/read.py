import csv

def convert_values_to_int(d):
    for key, value in d.items():
        try:
            d[key] = int(value)
        except ValueError:
            d[key] = value
    return d

def read_csv(file_path):
    """
    Read data from a CSV file and return it as a list of dictionaries.
    Convert strings to appropriate data types.
    
    :param file_path: Path to the CSV file
    :return: List of dictionaries containing the data
    """
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [convert_values_to_int(row) for row in csv_reader]
    return data