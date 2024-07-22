import csv

def write_csv(file_path, data):
    """
    Given function
    Write data to a CSV file.
    
    :param file_path: Path to the CSV file
    :param data: List of dictionaries containing the data to write
    """
    if data:
        keys = data[0].keys()
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
