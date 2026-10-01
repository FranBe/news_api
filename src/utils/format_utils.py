import json

def is_valid_json(json_string):
    """ Check if a string is json or not
    
    Returns: 
        true: in json format
        false: string is not in json format
    """

    try:
        json.loads(json_string)
        return True
    except (ValueError, TypeError, json.JSONDecodeError):
        return False