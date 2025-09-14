from typing import List


def validate_request(keys: dict, store: dict) -> None:
    for key in keys:
        if key not in store:
            if type(keys) == dict:
                raise Exception(f"{keys[key]} is required.", True)
            else:
                raise Exception(f"{key} is required.", True)