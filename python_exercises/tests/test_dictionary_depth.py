import unittest

from tasks.dictionary_depth import extract_keys_with_depth


class TestExtractKeysWithDepth(unittest.TestCase):
    
    def test_flat_dictionary(self):
        json_data = {
            "name": "John",
            "age": 30
        }
        expected_output = {
            'name': 0,
            'age': 0
        }
        
        self.assertEqual(extract_keys_with_depth(json_data), expected_output)

    def test_nested_dictionary(self):
        json_data = {
            "type": {
                "street": "123 Main St",
                "city": "Anytown"
            }
        }
        expected_output = {
            'type': 0,
            'type__street': 1,
            'type__city': 1
        }
        self.assertEqual(extract_keys_with_depth(json_data), expected_output)

    def test_list_of_dictionaries(self):
        json_data = {
            "phoneNumbers": [
                {"type": "home", "number": "123-456-7890"},
                {"type": "work", "number": "987-654-3210"}
            ]
        }
        expected_output = {
            'phoneNumbers': 0,
            'phoneNumbers__type': 1,
            'phoneNumbers__number': 1,
            'phoneNumbers__type': 1,
            'phoneNumbers__number': 1
        }
        self.assertEqual(dict(extract_keys_with_depth(json_data)), dict(expected_output))

    def test_complex_structure(self):
        json_data = {
            "name": "John",
            "age": 30,
            "type": {
                "street": "123 Main St",
                "city": "Anytown",
                "postalCode": "12345"
            },
            "phoneNumbers": [
                {"type": "home", "number": "123-456-7890"},
                {"type": "work", "number": "987-654-3210"}
            ]
        }
        expected_output = {
            'name': 0,
            'age': 0,
            'type': 0,
            'type__street': 1,
            'type__city': 1,
            'type__postalCode': 1,
            'phoneNumbers': 0,
            'phoneNumbers__type': 1,
            'phoneNumbers__number': 1,
            'phoneNumbers__type': 1,
            'phoneNumbers__number': 1
        }

        self.assertEqual(extract_keys_with_depth(json_data), expected_output)

    def test_empty_dictionary(self):
        json_data = {}
        expected_output = {}
        self.assertEqual(extract_keys_with_depth(json_data), expected_output)

    def test_complex_structure_failure(self):
        json_data = {
            "name": "John",
            "age": 30,
            "type": {
                "street": "123 Main St",
                "city": "Anytown",
                "postalCode": "12345"
            },
            "phoneNumbers": [
                {"type": "home", "number": "123-456-7890"},
                {"type": "work", "number": "987-654-3210"}
            ]
        }
        expected_output = {
            'name': 0,
            'age': 0,
            'type': 0,
            'type__street': 1,
            'type__city': 1,
            'type__postalCode': 1,
            'phoneNumbers': 0,
            'phoneNumbers': 1,
            'phoneNumbers__type': 2,
            'phoneNumbers__number': 2,
            'phoneNumbers': 1,
            'phoneNumbers__type': 2,
            'phoneNumbers__number': 2
        }
        self.assertNotEqual(dict(extract_keys_with_depth(json_data)), dict(expected_output))

if __name__ == '__main__':
    unittest.main()