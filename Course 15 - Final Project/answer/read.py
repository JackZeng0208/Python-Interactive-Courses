import csv

def convert_values_to_int(d):
    """
    Convert string values in a dictionary to integers if possible.
    
    :param d: Dictionary containing string values
    :return: Dictionary with string values converted to integers
    
    Note: If a value cannot be converted to an integer, it remains unchanged.
    """
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
    
    Note: don't forget to convert values to integers if possible, using the convert_values_to_int function
    """
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [convert_values_to_int(row) for row in csv_reader]
    return data