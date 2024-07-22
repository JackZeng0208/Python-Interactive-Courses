import csv

def write_csv(file_path, data):
    """
    Write data to a CSV file.
    
    :param file_path: Path to the CSV file
    :param data: List of dictionaries containing the data to write
    """
    # DON'T MODIFY THIS FUNCTION!
    if data:
        keys = data[0].keys()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
