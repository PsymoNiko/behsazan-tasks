import unittest

def get_depths(data, depth=1):
    if isinstance(data, dict):
        return {key: get_depths(value, depth + 1) for key, value in data.items()}
    elif isinstance(data, list):
        return [get_depths(item, depth + 1) for item in data]
    else:
        return depth  # Replace values with their depth

def create_depth_keys(data):
    detailed_depths = get_depths(data)
    
    # Create additional depth keys based on the original structure
    depth_keys = {f"{key}_dept": 1 for key in data.keys()}
    
    # Combine the detailed depths and the depth keys
    combined_result = {**detailed_depths, **depth_keys}
    
    return combined_result

class TestCreateDepthKeys(unittest.TestCase):

    def test_simple_dict(self):
        data = {'a': 1, 'b': 2}
        expected = {
            'a': 1,
            'b': 1,
            'a_dept': 1,
            'b_dept': 1
        }
        result = create_depth_keys(data)
        self.assertEqual(result, expected)

    def test_nested_dict(self):
        data = {
            'a': 1,
            'b': {
                'c': 2,
                'd': {
                    'e': 3
                }
            }
        }
        expected = {
            'a': 1,
            'b': {
                'c': 2,
                'd': {
                    'e': 3
                }
            },
            'a_dept': 1,
            'b_dept': 1
        }
        result = create_depth_keys(data)
        self.assertEqual(result, expected)

    def test_list_of_dicts(self):
        data = {
            'a': 1,
            'b': [
                {'c': 2},
                {'d': 3}
            ]
        }
        expected = {
            'a': 1,
            'b': [
                {'c': 2},
                {'d': 3}
            ],
            'a_dept': 1,
            'b_dept': 1
        }
        result = create_depth_keys(data)
        self.assertEqual(result, expected)

    def test_complex_structure(self):
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
        expected = {
            'name': 1,
            'age': 1,
            'address': {
                'street': 1,
                'city': 1,
                'postalCode': 1
            },
            'phoneNumbers': [
                {'type': 1, 'number': 1},
                {'type': 1, 'number': 1},
                {'title': [
                    {'type': 1, 'number': 1},
                    {'type': {
                        'street': 1,
                        'city': 1,
                        'postalCode': 1
                    }, 'number': 1}], 'duration': 1}
            ],
            'name_dept': 1,
            'age_dept': 1,
            'address_dept': 1,
            'phoneNumbers_dept': 1
        }
        result = create_depth_keys(json_data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
