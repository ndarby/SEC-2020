import json


def parse(filepath):
    """
    some docstring
    :param filepath: the file path to find the .json file
    :return: dict representing the JSON object
    """
    with open(filepath, 'r') as json_file:
        obj = json.load(json_file)
    return obj
