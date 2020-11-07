import csv


def parse(filepath):
    """
    Some docstring
    :param filepath: the file path to find the .csv file
    :return: list of dicts each containing the values of a row indexed by column name
    """
    with open(filepath, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]
    return rows
