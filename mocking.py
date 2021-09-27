# import requests
# import json
# response = requests.get()

response = {
    "data": [
        {"name": "name_1"},
        {"name": "name_2"},
        {"name": "name_3"},
        {"name": "name_4", "data": [
            {"name": "name_5"},
            {"name": "name_7"},
            {"name": "name_8", "data": [
                {"name": "name_9"},
                {"name": "name_10", "data": [
                    {"name": "name_11"},
                    {"name": "name_12"},
                    {"name": "name_13"},
                    {"name": "name_14", "data": {
                        "res": "ok"
                    }}
                ]}
            ]}
        ]}
    ],
    "name": "name"
}
# print(response.keys())
# print(response.items())
# print(response.values())
def mock(data,):
    for obj in data:
        print(obj)
        for key in obj.keys():
            value = obj[key]
            print(value)
            if type(value) == list:
                mock(value)


for key in response.keys():
    value = response[key]


    if type(value) == list:
        mock(response[key])


