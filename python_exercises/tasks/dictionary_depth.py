def extract_keys_with_depth(d, depth=0, parent_key=''):
    keys_with_depth = dict()
    
    for key, value in d.items():
        full_key = f"{parent_key}__{key}" if parent_key else key
        keys_with_depth[full_key] = depth
        
        if isinstance(value, dict):
            keys_with_depth.update(extract_keys_with_depth(value, depth + 1, full_key))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    keys_with_depth.update(extract_keys_with_depth(item, depth + 1, full_key))

    return keys_with_depth


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
result = extract_keys_with_depth(json_data)
