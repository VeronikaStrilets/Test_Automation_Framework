import json


def json_to_dict(json_str):
    """Convert JSON string to dictionary."""
    return json.loads(json_str)


def dict_to_json(json_dict):
    """Convert dictionary to JSON string."""
    return json.dumps(json_dict)
