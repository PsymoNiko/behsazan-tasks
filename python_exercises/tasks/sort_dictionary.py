
# def get_depths(data, depth=1):
#     """
#     Recursively traverses a nested dictionary and returns a dictionary with the same structure,
#     but with keys replaced by their corresponding depths.

#     Args:
#         data: The input dictionary.
#         depth: The current depth in the recursion (default is 1).

#     Returns:
#         A dictionary with the same structure as the input, but with keys replaced by depths.
#     """
#     if isinstance(data, dict):
#         return {key: get_depths(value, depth + 1) for key, value in data.items()}
#     elif isinstance(data, list):
#         return [get_depths(item, depth + 1) for item in data]
#     else:
#         return depth  # Replace values with their depth

# def create_depth_keys(data):
#     """
#     Creates a dictionary with the depth of each top-level key and appends additional keys in the format {key}_dept.

#     Args:
#         data: The input dictionary.

#     Returns:
#         A combined dictionary with the structure and additional depth keys.
#     """
#     # Get the detailed depths
#     detailed_depths = get_depths(data)
    
#     # Create additional depth keys
#     depth_keys = {f"{key}_depth": 1 for key in data.keys()}
    
#     # Combine the detailed depths and the depth keys
#     combined_result = {**detailed_depths, **depth_keys}
    
#     return combined_result

# # Example usage
# json_data = {
#     "name": "John",
#     "age": 30,
#     "address": {
#         "street": "123 Main St",
#         "city": "Anytown",
#         "postalCode": "12345"
#     },
#     "phoneNumbers": [
#         {"type": "home", "number": "123-456-7890"},
#         {"type": "work", "number": "987-654-3210"},
#         {"title": [{"type": "work", "number": "987-654-3210"},
#                    {"type": {
#                        "street": "123 Main St",
#                        "city": "Anytown",
#                        "postalCode": "12345"
#                    }, "number": "987-654-3210"}], "duration": "six mo"}
#     ]
# }

# # Call the create_depth_keys function
# result = create_depth_keys(json_data)
# print(result)


def get_depths(data, depth=1):
    """
    Recursively traverses a nested dictionary and returns a dictionary with the same structure,
    but with keys replaced by their corresponding depths.

    Args:
        data: The input dictionary.
        depth: The current depth in the recursion (default is 1).

    Returns:
        A dictionary with the same structure as the input, but with keys replaced by depths.
    """
    if isinstance(data, dict):
        return {key: get_depths(value, depth + 1) for key, value in data.items()}
    elif isinstance(data, list):
        return [get_depths(item, depth + 1) for item in data]
    else:
        return depth  # Replace values with their depth

def create_depth_keys(data):
    """
    Creates a dictionary with the depth of each top-level key and appends additional keys in the format {key}_dept.

    Args:
        data: The input dictionary.

    Returns:
        A combined dictionary with the structure and additional depth keys.
    """
    # Get the detailed depths
    detailed_depths = get_depths(data)
    
    # Create additional depth keys
    depth_keys = {f"{key}_dept": 1 for key in data.keys()}
    
    # Combine the detailed depths and the depth keys
    combined_result = {**detailed_depths, **depth_keys}
    
    return combined_result

# Example usage
json_data = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "postalCode": "12345"
    },
    "phoneNumbers": [
        {"type": "home", "number": "123-456-7890"},
        {"type": "work", "number": "987-654-3210"},
        {"title": [{"type": "work", "number": "987-654-3210"},
                   {"type": {
                       "street": "123 Main St",
                       "city": "Anytown",
                       "postalCode": "12345"
                   }, "number": "987-654-3210"}], "duration": "six mo"}
    ]
}

# Call the create_depth_keys function
result = create_depth_keys(json_data)
print(result)
