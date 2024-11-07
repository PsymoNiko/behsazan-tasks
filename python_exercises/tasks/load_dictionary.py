import json
import sys
import importlib.util
from pathlib import Path
import os

def read_dict_from_file(filename: str):
    """Reads a dictionary from a JSON or Python file.

    Args:
        filename (str): The path to the JSON or Python file.

    Raises:
        ValueError: If the file type is not supported or if the Python file does not contain a variable named 'dict'.

    Returns:
        dict: The dictionary read from the file.
    """
    print(f"Reading from: {filename}")
    
    # Check the file extension
    _, file_extension = os.path.splitext(filename)
    
    if file_extension == '.json':
        # Read from a JSON file
        with open(filename, 'r') as file:
            data = json.load(file)
    elif file_extension == '.py':
        # Read from a Python module
        if not os.path.isfile(filename):
            raise FileNotFoundError(f"The file {filename} does not exist.")
    

        module_name =  Path(filename).name
        spec = importlib.util.spec_from_file_location(module_name, filename)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        data = module.my_dict

    else:
        raise ValueError("Unsupported file type. Please provide a .json or .py file.")
    
    return data

# Example usage
try:
    json_data = read_dict_from_file('utils/utils.json')
    print("Contents of the JSON file:\n_________________________________________")
    print(json.dumps(json_data, indent=4))
    
    python_data = read_dict_from_file('utils/utils.py')
    print("Contents of the Python file:\n_________________________________________")
    print(python_data)
except Exception as e:
    print(f"Error: {e}")





# import importlib.util
# import sys

# def load_module(module_name, file_path):
#     spec = importlib.util.spec_from_file_location(module_name, file_path)
#     module = importlib.util.module_from_spec(spec)
#     sys.modules[module_name] = module
#     spec.loader.exec_module(module)
#     return module


# file_path = 'utils/utils.py'
# # module_name = 'utils.py'
# module_name = Path(file_path).name



# loaded_module = load_module(module_name, file_path)
# my_dict_value = loaded_module.my_dict

# print("032940-2394329-0492-0492-03940-32")
# print(my_dict_value)