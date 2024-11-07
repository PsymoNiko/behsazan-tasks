from datetime import datetime as dt


my_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "postalCode": "12345"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "123-456-7890"
        },
        {
            "type": "work",
            "number": "987-654-3210"
        }
    ],
    "timestamp": dt.now()
}

print("my_dict is: ", my_dict)
