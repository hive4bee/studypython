import json
file_path="/home/eprot/py/sample2.json"
with open(file_path, "r") as json_file:
    json_data=json.load(json_file)
    print(json_data)
    print("")
    print(json_data["posts"])
    print()
    print(json_data["posts"][0]['title'])