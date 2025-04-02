import yaml
import json


formats = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load}


def convertator(data, extension):
    """
    Сonverts files of different formats into a python dictionary
    """
    if extension not in formats:
        raise ValueError('Unsupported format. Next formats are supported: {}'
                         .format(formats.keys()))
    return formats[extension](data)
